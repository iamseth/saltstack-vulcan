import os
import shutil
import tempfile
import unittest

from vulcan.formula import Formula

class TestFormula(unittest.TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self):
        if os.path.isdir(self.tempdir):
            shutil.rmtree(self.tempdir)

    def test_create_from_dict(self):
        data = {'name': 'test', 'url': 'http://test.com'}
        formula = Formula.from_dict(data)
        self.assertEqual(formula.name, 'test')
        self.assertEqual(formula.branch, 'master')
        self.assertEqual(formula.revision, 'HEAD')

    def test_is_installed_not_installed(self):
        data = {'name': 'test', 'url': 'http://test.com', 'install_directory': self.tempdir}
        formula = Formula.from_dict(data)
        self.assertFalse(formula.is_installed())

    def test_is_icurrent_not_installed(self):
        data = {'name': 'test', 'url': 'http://test.com', 'install_directory': self.tempdir}
        formula = Formula.from_dict(data)
        self.assertFalse(formula.is_current())

if __name__ == '__main__':
    unittest.main()
