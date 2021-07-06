# Тестирование функции Concurrency для Concurrency1.py
import unittest
import random
from Concurrency1 import Concurrency

class Simultaneous(unittest.TestCase):

    def setUp(self):
        self.Number_tests = random.randint(1, 10)    # случайное число тестов
        self.Lenght_Massiv = random.randint(1, 200)    # случайный размер входного массива

    def Rounding(self,number):    # округление вещественных чисел до 6-го знака
        number = int(number * 1000000) / 1000000
        return number


# 1. Покрытие в широком диапазоне
    def test_regression1(self):
        for i in range(self.Number_tests):
            N0 = random.randint(2, 10)    # случайное число процессов (экземпляров ф-ии )
            L0 = []
            for i in range(self.Lenght_Massiv):    # формируем входной массив вещественных чисел
                L0.append(random.uniform(0, 100))
            rez1 = 0    # обычное суммирование массива циклом
            for i in L0:
                rez1 += i
            rez1 = self.Rounding(rez1)
            rez2 = self.Rounding(Concurrency(N0, L0))
            self.assertEqual(rez1, rez2)

if __name__ == '__main__':
    unittest.main()