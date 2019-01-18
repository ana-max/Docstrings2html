

class ExceptionChecker(Exception):
    def __init__(self, text):
        self.txt = text

    def _is_correct_bracket_seq(self):
        """Проверка на корректную скобочную последовательность"""

    def _is_correct_input_syms(self):
        """Проверка на вхождение недопустимых символов"""

    def _is_correct_polynomial(self):
        """Проверка на корректность математических операций"""

    def is_correct(self):
        pass
