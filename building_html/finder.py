from collections import namedtuple
import re
import ast
Class = namedtuple('Class', 'name docstrings functions')
Function = namedtuple('Function', 'name docstrings arguments')
reg_for_arguments = re.compile(r'\(.*\)')


class Finder:
    def __init__(self, filename):
        self.functions_out_classes = list()
        self.classes = list()
        self.code_tree = {'out_classes': list(),
                          'in_classes': list()}
        with open(filename, encoding='utf-8') as f:
            file_contents = f.read()
        self.filename = filename
        self.module = ast.parse(file_contents)
        with open(self.filename, encoding='utf-8') as f:
            self.content = f.readlines()

    def get_code_tree(self):
        self._get_functions_out_classes()
        self._get_classes_with_functions()
        self.code_tree['in_classes'] = self.classes
        self.code_tree['out_classes'] = self.functions_out_classes
        return self.code_tree

    def _get_functions_out_classes(self):
        self.functions_out_classes =\
            [Function(node.name,
                      ast.get_docstring(node),
                      self._get_args_of_ast_function(node))
             for node in self.module.body
             if isinstance(node, ast.FunctionDef)]

    def _get_classes_with_functions(self):
        class_definitions = [node for node in self.module.body if
                             isinstance(node, ast.ClassDef)]
        for c in class_definitions:
            self.classes\
                .append(Class(c.name, ast.get_docstring(c),
                              [Function(node.name,
                                        ast.get_docstring(node),
                                        self._get_args_of_ast_function(node))
                               for node in c.body
                               if isinstance(node, ast.FunctionDef)]))

    def _get_args_of_ast_function(self, function):
        description_of_function = self.content[function.lineno-1:]
        args = ['']
        flag = False
        for i in range(len(description_of_function)):
            if 'def' in description_of_function[i]:
                strings_of_arguments = list()
                if '(' in description_of_function[i]:
                    for j in range(i, len(description_of_function)):
                        strings_of_arguments.append(description_of_function[j])
                        if ')' in description_of_function[j]:
                            flag = True
                            all_args = ''.join(strings_of_arguments)
                            args = re.findall(reg_for_arguments,
                                              all_args.replace('\n', ''))
                            break
            if flag:
                break
        return args[0]
