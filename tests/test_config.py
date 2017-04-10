import unittest

import vulcan.config

class TestConfig(unittest.TestCase):

    def test_newconfig(self):
        cfg = vulcan.config.Config('./tests/data/vulcan.yaml')
        self.assertEqual(len(cfg.formulas), 3)

if __name__ == '__main__':
    unittest.main()
