from building_html.finder import Finder
from parser_filenames import Parser
import shutil
from contextlib import suppress
from building_html import html_builder
import unittest


class BuilderTest(unittest.TestCase):
    def setUp(self):
        self.testing_filename = ['./testing_filename.py']
        self.testing_directory_name = ['./testing_directory']
        self.finder = Finder

    def test_structure(self):
        parser = Parser(self.testing_directory_name)
        with suppress(FileNotFoundError):
            shutil.rmtree('documentation')
        structure = parser.get_directories_structure()
        builder = html_builder.Builder(structure)
        builder.get_all_information()
        self.assertEqual(list(builder.information['testing_directory'].keys()),
                         ['Parser.py',
                          'PolynomialExceptions.py'])

    def test_information(self):
        parser = Parser(self.testing_filename)
        with suppress(FileNotFoundError):
            shutil.rmtree('documentation')
        structure = parser.get_directories_structure()
        builder = html_builder.Builder(structure)
        builder.get_all_information()
        self.assertEqual(list(builder.information.keys()),
                         ['testing_filename.py'])


if __name__ == '__main__':
    unittest.main()
