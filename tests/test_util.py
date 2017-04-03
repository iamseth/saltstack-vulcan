import os
import shutil
import random
import string
import tempfile
import unittest

from vulcan import util

def random_string():
    return ''.join([string.letters[random.randint(0, len(string.letters)-1)] for c in xrange(18)])

class TestUtil(unittest.TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self):
        if os.path.isdir(self.tempdir):
            shutil.rmtree(self.tempdir)

    def test_hashfile(self):
        temp_file = os.path.join(self.tempdir, random_string())
        with open(temp_file, 'w') as fh:
            fh.write('test')
        self.assertEqual(util.hashfile(temp_file), 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3')

    def test_hashdir(self):
        temp_file = os.path.join(self.tempdir, random_string())
        with open(temp_file, 'w') as fh:
            fh.write('test')
        self.assertEqual(util.hashdir(self.tempdir), 'c4033bff94b567a190e33faa551f411caef444f2')

    def test_hashdir_excludes(self):
        filename = random_string()
        temp_file = os.path.join(self.tempdir, filename)
        with open(temp_file, 'w') as fh:
            fh.write('test')
        self.assertEqual(util.hashdir(self.tempdir, file_excludes=[filename]), 'da39a3ee5e6b4b0d3255bfef95601890afd80709')

if __name__ == '__main__':
    unittest.main()
