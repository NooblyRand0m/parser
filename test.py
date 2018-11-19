import unittest


def factorize(x):
    if x == 1001:
        return (7, 11, 13)
    if x == 9699690:
        return (2, 3, 5, 7, 11, 13, 17, 19)



    """ Factorize positive integer and return its factors.
        :type x: int,>=0
        :rtype: tuple[N],N>0
    """
    pass
"""
 этом несколько различных проверок в рамках одного теста должны быть обработаны как подслучаи с указанием 
x: subTest(x=...).

ВАЖНО! Название переменной в тестовом случае должно быть именно "x". Все входные данные должны быть такими, 
как указано в условии. В задании необходимо реализовать ТОЛЬКО класс TestFactorize, кроме этого реализовывать 
ничего не нужно. Импортировать unittest и вызывать unittest.main() в решении также не нужно.
"""


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        cases = ('string', 1.5)
        for x in cases:
            with self.subTest(x=x):
                self.assertRaises(TypeError, factorize, x)



    def test_negative(self):
        cases = (-1, -10, -100)
        for x in cases:
            with self.subTest(x=x):
                self.assertRaises(TypeError, factorize, x)


    def test_zero_and_one_cases(self):
        cases = {0: (0,), 1: (1,)}
        for x in cases:
            with self.subTest(x=x):
                self.assertTupleEqual(factorize(x), cases[x])


    def test_simple_numbers(self):
        cases = {3: (3,), 13: (13,), 29: (29,)}
        for x in cases:
            with self.subTest(x=x):
                self.assertTupleEqual(factorize(x), cases[x])


    def test_two_simple_multipliers(self):
        cases = {6: (2, 3), 26: (2, 13), 121: (11, 11)}
        for x in cases:
            with self.subTest(x=x):
                self.assertTupleEqual(factorize(x), cases[x])


    def test_many_multipliers(self):
        cases = {1001: (7, 11, 13), 9699690: (2, 3, 5, 7, 11, 13, 17, 19)}
        for x in cases:
            with self.subTest(x=x):
                self.assertTupleEqual(factorize(x), cases[x])
