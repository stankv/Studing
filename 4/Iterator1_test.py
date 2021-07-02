# Тестирование класса List2 для Iterator1.py
import unittest
import random
from Iterator1 import List2

class Iter1(unittest.TestCase):

# Покрытие в широком диапазоне
    def test_regression1_1(self):
        for j in range(10000):    # количество повторений теста
            N = random.randint(1, 100)
            l2 = List2(N)
            il2 = iter(l2)
            result1 = []
            for i in range(10):
                result1.append(N)
                N *= 2
            result2 = []
            for i in range(10):
                result2.append(next(il2))
            self.assertEqual(result1, result2)

if __name__ == '__main__':
    unittest.main()