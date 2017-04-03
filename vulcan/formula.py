import os
import json
import shutil
import logging
import tempfile

import git

from vulcan import util

log = logging.getLogger(__name__)

class Formula(object):
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.branch = 'master'
        self.revision = 'HEAD'
        self.origin_name = name
        self.install_directory = 'formulas'

    @property
    def state_file(self):
        '''Helper property for the state file path.
        '''
        return os.path.join(self.install_directory, self.name, 'state.json')

    def is_installed(self):
        '''Check to see if the formula is already installed.
        '''
        if os.path.isfile(self.state_file):
            return True
        return False

    def is_current(self):
        '''Determine if the formula is current with the configuration.

        '''
        # If revision set to HEAD, just assume not current.
        # We could query upstream to see if the revision is out of date
        # however this results in less code and complexity at the expense of extra Git clones.
        if self.revision == 'HEAD':
            return False

        # If not installed, of course not current.
        if not self.is_installed():
            return False


        # Open the state.json file and compare values to config.
        # If any value differs, consider the formula not current.
        with open(self.state_file, 'r') as fh:
            state = json.load(fh)
            if state.get('checksum') != self.checksum():
                log.info('Checksums differ for %s.', self.name)
            for key in ('name', 'origin_name', 'url', 'branch', 'revision'):
                if state.get(key) != self.__dict__.get(key):
                    return False

        return True

    def install(self, force=False):
        '''Install formula if not already installed. Will not update if out of date.
        '''
        if not force and self.is_installed():
            return

        log.info('Installing formula %s', self.name)
        # Clone the repository to a temp directory.
        tmpdir = tempfile.mkdtemp()
        try:
            repo = git.Repo.clone_from(url=self.url, to_path=tmpdir, branch=self.branch)
            repo.head.reset(commit=self.revision, index=True, working_tree=True)

            # Remove existing install for a clean install.
            destination = os.path.join(self.install_directory, self.name)
            if os.path.isdir(destination):
                shutil.rmtree(destination)

            # Move formula into place.
            origin = os.path.join(tmpdir, self.origin_name)
            shutil.move(origin, destination)

            # Save state file.
            with open(self.state_file, 'w') as fh:
                json.dump(self.as_dict(), fh)

        finally:
            if os.path.isdir(tmpdir):
                shutil.rmtree(tmpdir)

    def update(self):
        '''Update formula if out of out of date. Will install if required.
        '''
        if self.is_current():
            return
        return self.install(force=True)

    def checksum(self):
        '''Determine the checksum for the formula.

        A checksum is a SHA1 hash of a list of hashes of files in the formula directory.
        '''
        path = os.path.join(self.install_directory, self.name)
        return util.hashdir(path, file_excludes=['state.json'])

    def as_dict(self):
        '''A dictionary representation of the Formula.
        '''
        return {'name': self.name,
                'origin_name': self.origin_name,
                'url': self.url,
                'branch': self.branch,
                'revision': self.revision,
                'install_directory': self.install_directory,
                'checksum': self.checksum()}

    @staticmethod
    def from_dict(data):
        '''Build a new Formula object from a dictionary.
        '''
        formula = Formula(name=data['name'], url=data['url'])
        if 'branch' in data:
            formula.branch = data['branch']
        if 'revision' in data:
            formula.revision = data['revision']
        if 'origin_name' in data:
            formula.origin_name = data['origin_name']
        if 'install_directory' in data:
            formula.install_directory = data['install_directory']
        return formula

    def __repr__(self):
        return self.name
