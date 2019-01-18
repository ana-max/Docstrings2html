import unittest
from parser_filenames import Parser


class ParserTest(unittest.TestCase):
    def setUp(self):
        self.testing_filename = ['./testing_filename.py']
        self.testing_directory_name = ['./testing_directory']
        self.parser = Parser

    def test_for_existing(self):
        parser = self.parser(['not_exist_file.py'])
        with self.assertRaises(FileNotFoundError):
            parser.get_directories_structure()

    def test_directories_structure_for_directory(self):
        parser = self.parser(self.testing_directory_name)
        expected = {'testing_directory':
                    ['.\\testing_directory\\Parser.py',
                     '.\\testing_directory\\PolynomialExceptions.py']}
        self.assertEqual(expected, parser.get_directories_structure())

    def test_directories_structure_for_file(self):
        parser = self.parser(self.testing_filename)
        expected = {'testing_filename.py': ['./testing_filename.py']}
        self.assertEqual(expected, parser.get_directories_structure())

    def test_get_structure_of_all(self):
        parser = self.parser([self.testing_directory_name[0],
                              self.testing_filename[0]])
        structure = parser.get_directories_structure()
        expected = {'testing_directory':
                    ['.\\testing_directory\\Parser.py',
                     '.\\testing_directory\\PolynomialExceptions.py'],
                    'testing_filename.py': ['./testing_filename.py']}
        self.assertEqual(expected, structure)

    def test_get_all_files_from_directory_and_file(self):
        parser = self.parser([self.testing_directory_name[0],
                              self.testing_filename[0]])
        files = list()
        for file in parser.names_of_files:
            files.append(parser.get_all_files(file))
        expected = [['.\\testing_directory\\Parser.py',
                    '.\\testing_directory\\PolynomialExceptions.py'],
                    ['./testing_filename.py']]
        self.assertEqual(expected, files)

    def test_work_with_directory(self):
        parser = self.parser(self.testing_directory_name)
        files = parser._work_with_directory(self.testing_directory_name[0])
        expected = ['.\\testing_directory\\Parser.py',
                    '.\\testing_directory\\PolynomialExceptions.py']
        self.assertEqual(expected, files)


if __name__ == '__main__':
    unittest.main()
