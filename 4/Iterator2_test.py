# Тестирование класса List2 для Iterator2.py
import unittest
import random
from Iterator2 import List2

class Iter1(unittest.TestCase):

# 1. Покрытие в широком диапазоне, flag = False (конечная последовательность)
    def test_regression1(self):
        flag1 = False
        for j in range(10000):    # количество повторений теста
            N1 = random.randint(1, 100)
            l2 = List2(N1, flag1)
            il2 = iter(l2)
            result1 = []
            s = 1
            for i in range(N1):
                result1.append(s)
                s *= 2
            result2 = []
            for i in range(N1):
                result2.append(next(il2))
            self.assertEqual(result1, result2)

# 2. Покрытие в широком диапазоне, flag = True (бесконечная последовательность)
    def test_regression2(self):
        flag1 = True
        for k in range(1000):    # количество повторений теста
            N1 = random.randint(1, 10)    # количество элементов последовательности
            N2 = random.randint(1, 10)    # количество последовательностей
            l2 = List2(N1, flag1)
            il2 = iter(l2)
            result1 = []
            for i in range(N2):
                s = 1
                for j in range(N1):
                    result1.append(s)
                    s *= 2
            result2 =[]
            for i in range(N1 * N2):
                result2.append(next(il2))
            self.assertEqual(result1, result2)

if __name__ == '__main__':
    unittest.main()