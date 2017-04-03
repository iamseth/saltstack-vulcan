import logging

from vulcan.formula import Formula

import yaml

log = logging.getLogger(__name__)


class Config(object):
    def __init__(self, config_path='vulcan.yaml'):
        with open(config_path, 'rb') as fh:
            self.cfg = yaml.load(fh)
            self.formulas = [Formula.from_dict(f) for f in self.cfg.get('formulas', [])]
