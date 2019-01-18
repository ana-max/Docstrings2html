import unittest
from building_html.finder import Finder
from building_html.finder import Function
from building_html.finder import Class


class FinderTest(unittest.TestCase):
    def setUp(self):
        self.testing_filename = './testing_filename.py'
        self.testing_directory_name = './testing_directory'
        self.finder = Finder

    def test_get_functions_out_classes_for_file(self):
        finder = self.finder(self.testing_filename)
        finder._get_functions_out_classes()
        functions = finder.functions_out_classes
        self.assertEqual(functions, [])

    def test_get_functions_out_classes_for_directory(self):
        finder = self.finder(self.testing_directory_name+'/Parser.py')
        finder._get_functions_out_classes()
        functions = finder.functions_out_classes
        expected = [Function(name='out_class',
                             docstrings=None,
                             arguments='()')]
        self.assertEqual(functions, expected)

    def test_get_classes_with_functions_with_eng_docstrings(self):
        finder = self.finder(self.testing_filename)
        finder._get_classes_with_functions()
        classes_with_functions = finder.\
            classes
        expected = [Class(name='AngleConverter',
                          docstrings=None,
                          functions=[Function(name='time_to_degree_time',
                                              docstrings=':param time: '
                                                         'Time\n:return: list',
                                              arguments='(self, time)'),
                                     Function(name='minutes_'
                                                   'conversion_to_degrees',
                                              docstrings='Convert '
                                                         'minutes to degrees',
                                              arguments='(self, minutes)'),
                                     Function(name='seconds'
                                                   '_conversion_to_degrees',
                                              docstrings=':param seconds:'
                                                         ' int\n:return: '
                                                         'float',
                                              arguments='(self, seconds)'),
                                     Function(name='time_to_hours'
                                                   '_and_piece_of_hour',
                                              docstrings='Convert '
                                                         'time to hour'
                                                         ' and piece of hour',
                                              arguments='(self, time)')])]
        self.assertEqual(classes_with_functions, expected)

    def test_get_classes_with_functions_with_rus_docstrings(self):
        finder = self\
            .finder(self.testing_directory_name+'/PolynomialExceptions.py')
        finder._get_classes_with_functions()
        classes_with_functions = finder.classes
        first_doc = 'Проверка на корректную скобочную последовательность'
        second_doc = 'Проверка на вхождение недопустимых символов'
        third_doc = 'Проверка на корректность математических операций'
        expected = [Class(name='ExceptionChecker',
                          docstrings=None,
                          functions=[Function(name='__init__',
                                              docstrings=None,
                                              arguments='(self, text)'),
                                     Function(name='_is_correct_bracket_seq',
                                              docstrings=first_doc,
                                              arguments='(self)'),
                                     Function(name='_is_correct_input_syms',
                                              docstrings=second_doc,
                                              arguments='(self)'),
                                     Function(name='_is_correct_polynomial',
                                              docstrings=third_doc,
                                              arguments='(self)'),
                                     Function(name='is_correct',
                                              docstrings=None,
                                              arguments='(self)')])]
        self.assertEqual(classes_with_functions, expected)

    def test_get_code_tree(self):
        finder = self\
            .finder(self.testing_directory_name+'/PolynomialExceptions.py')
        code_tree = finder.get_code_tree()
        first_doc = 'Проверка на корректную скобочную последовательность'
        second_doc = 'Проверка на вхождение недопустимых символов'
        third_doc = 'Проверка на корректность математических операций'
        exp_in = [Class(name='ExceptionChecker',
                        docstrings=None,
                        functions=[Function(name='__init__',
                                            docstrings=None,
                                            arguments='(self, text)'),
                                   Function(name='_is_correct_bracket_seq',
                                            docstrings=first_doc,
                                            arguments='(self)'),
                                   Function(name='_is_correct_input_syms',
                                            docstrings=second_doc,
                                            arguments='(self)'),
                                   Function(name='_is_correct_polynomial',
                                            docstrings=third_doc,
                                            arguments='(self)'),
                                   Function(name='is_correct',
                                            docstrings=None,
                                            arguments='(self)')])]
        exp_out = []
        expected = {'out_classes': exp_out, 'in_classes': exp_in}
        self.assertEqual(code_tree, expected)


if __name__ == '__main__':
    unittest.main()
