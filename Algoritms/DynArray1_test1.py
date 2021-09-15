# Тестирование функции вставки элемента insert(i, itm)
import unittest
from DynArray1 import DynArray

class insert_test(unittest.TestCase):

# РЕГРЕССИОННЫЕ ТЕСТЫ

# 1. Пустой массив, вставка в 0-ю позицию
    def test_regression1(self):
        da = DynArray()
        da.insert(0, 1000)
        self.assertEqual(da[0], 1000)

# Вставка элемента, когда в итоге размер буфера не превышен ------------------------------------------------------
# размер буфера = 32, начальное число элементов массива 25

# 2. Вставка в 0-ю позицию
    def test_regression2(self):
        da = make_da(25)
        da.insert(0, 1000)
        self.assertEqual(da[0], 1000)

# 2.2. Проверка размера буфера после вставки (сравнение до и после)
    def test_regression2_2(self):
        da = make_da(25)
        a = da.capacity
        da.insert(0, 1000)
        b = da.capacity
        self.assertEqual(a, b)

# 3. Вставка в 1-ю позицию
    def test_regression3(self):
        da = make_da(25)
        da.insert(1, 1000)
        self.assertEqual(da[1], 1000)

# 4. Вставка в середину
    def test_regression4(self):
        da = make_da(25)
        da.insert(15, 1000)
        self.assertEqual(da[15], 1000)

# 5. Вставка в предпоследнюю позицию
    def test_regression5(self):
        da = make_da(25)
        da.insert(23, 1000)
        self.assertEqual(da[23], 1000)

# 6. Вставка в последнюю позицию
    def test_regression6(self):
        da = make_da(25)
        da.insert(24, 1000)
        self.assertEqual(da[24], 1000)

# 7. Вставка в позицию, равную длине рабочего массива
    def test_regression7(self):
        da = make_da(25)
        da.insert(25, 1000)
        self.assertEqual(da[25], 1000)

# 8. Попытка вставки элемента в недопустимую позицию
    def test_regression8(self):
        da = make_da(25)
        try:
            da.insert(100, 1000)
        except IndexError:
            self.assertEqual(da[0], 0)

# Вставка элемента, когда в результате превышен размер буфера ------------------------------------------------------
#  начальный размер буфера = 32, начальное число элементов массива 32

# 9. Вставка в 0-ю позицию
    def test_regression9(self):
        da = make_da(32)
        da.insert(0, 1000)
        self.assertEqual(da[0], 1000)

# 9.1. Проверка размера буфера после вставки в 0-ю позицию (сравнение до и после)
    def test_regression9_1(self):
        da = make_da(16)
        a = da.capacity    # = 16 до вставки
        da.insert(0, 1000)
        b = da.capacity    # = 32 после
        self.assertEqual(a * 2, b)

# 9.2. Проверка количества элементов после вставки в 0-ю позицию (сравнение до и после)
    def test_regression9_2(self):
        da = make_da(16)
        a = da.count    # = 16 до вставки
        da.insert(0, 1000)
        b = da.count    # = 17 после
        self.assertEqual(a + 1, b)

# 10. Вставка в 1-ю позицию
    def test_regression10(self):
        da = make_da(16)
        da.insert(1, 1000)
        self.assertEqual(da[1], 1000)

# 10.1. Проверка размера буфера после вставки в 1-ю позицию (сравнение до и после)
    def test_regression10_1(self):
        da = make_da(16)
        a = da.capacity    # = 16 до вставки
        da.insert(1, 1000)
        b = da.capacity    # = 32 после
        self.assertEqual(a * 2, b)

# 10.2. Проверка количества элементов после вставки в 1-ю позицию (сравнение до и после)
    def test_regression10_2(self):
        da = make_da(16)
        a = da.count    # = 16 до вставки
        da.insert(1, 1000)
        b = da.count    # = 17 после
        self.assertEqual(a + 1, b)

# 11. Вставка в середину
    def test_regression11(self):
        da = make_da(32)
        da.insert(15, 1000)
        self.assertEqual(da[15], 1000)

# 11.1. Проверка размера буфера после вставки в середину (сравнение до и после)
    def test_regression11_1(self):
        da = make_da(16)
        a = da.capacity    # = 16 до вставки
        da.insert(8, 1000)
        b = da.capacity    # = 32 до вставки
        self.assertEqual(a * 2, b)

# 11.2. Проверка количества элементов после вставки в середину (сравнение до и после)
    def test_regression11_2(self):
        da = make_da(16)
        a = da.count    # = 16 до вставки
        da.insert(8, 1000)
        b = da.count    # = 17 после
        self.assertEqual(a + 1, b)

# 12. Вставка в предпоследнюю позицию
    def test_regression12(self):
        da = make_da(32)
        da.insert(30, 1000)
        self.assertEqual(da[30], 1000)

# 12.1. Проверка размера буфера после вставки в предпоследнюю позицию (сравнение до и после)
    def test_regression12_1(self):
        da = make_da(16)
        a = da.capacity    # = 16 до вставки
        da.insert(14, 1000)
        b = da.capacity    # = 32 до вставки
        self.assertEqual(a * 2, b)

# 12.2. Проверка количества элементов после вставки в предпоследнюю позицию (сравнение до и после)
    def test_regression12_2(self):
        da = make_da(16)
        a = da.count    # = 16 до вставки
        da.insert(14, 1000)
        b = da.count    # = 17 после
        self.assertEqual(a + 1, b)

# 13. Вставка в последнюю позицию
    def test_regression13(self):
        da = make_da(32)
        da.insert(31, 1000)
        self.assertEqual(da[31], 1000)

# 13.1. Проверка размера буфера после вставки в последнюю позицию (сравнение до и после)
    def test_regression13_1(self):
        da = make_da(16)
        a = da.capacity    # = 16 до вставки
        da.insert(15, 1000)
        b = da.capacity    # = 32 до вставки
        self.assertEqual(a * 2, b)

# 13.2. Проверка количества элементов после вставки в последнюю позицию (сравнение до и после)
    def test_regression13_2(self):
        da = make_da(16)
        a = da.count    # = 16 до вставки
        da.insert(15, 1000)
        b = da.count    # = 17 после
        self.assertEqual(a + 1, b)

# 14. Вставка в позицию, равную длине рабочего массива
    def test_regression14(self):
        da = make_da(16)
        da.insert(16, 1000)
        self.assertEqual(da[16], 1000)

# 14.1. Проверка размера буфера после вставки в позицию, равную длине рабочего массива (сравнение до и после)
    def test_regression14_1(self):
        da = make_da(16)
        a = da.capacity    # = 16 до вставки
        da.insert(16, 1000)
        b = da.capacity    # = 32 до вставки
        self.assertEqual(a * 2, b)

# 14.2. Проверка количества элементов после вставки в позицию, равную длине рабочего массива (сравнение до и после)
    def test_regression14_2(self):
        da = make_da(16)
        a = da.count    # = 16 до вставки
        da.insert(16, 1000)
        b = da.count    # = 17 после
        self.assertEqual(a + 1, b)

# 15. Вставка в позицию, равную длине рабочего массива после вставки в середину
    def test_regression15(self):
        da = make_da(16)
        da.insert(8, 1000)
        da.insert(da.count, 0)
        self.assertEqual(da[17], 0)
#-----------------------------------------------------------------------------------------------------------------------

# 16. Попытка вставки элемента в недопустимую позицию
    def test_regression16(self):
        da = make_da(32)
        try:
            da.insert(100, 1000)
        except IndexError:
            self.assertEqual(da[0], 0)
#------------------------------------------------------------------------------------------------------------------------

# Ф-я формирования и заполнения динамического массива
def make_da(number):
    S = DynArray()
    for i in range(number):
        S.append(i)
    return S

if __name__ == '__main__':
    unittest.main()