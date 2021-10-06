# ФИЛЬТР БЛЮМА НА ОСНОВЕ БИТОВОГО МАССИВА
# (входные данные - строки)
import bitarray

class BloomFilter:

    # создаём битовый массив длиной f_len
    def __init__(self, f_len):
        self.filter_len = f_len
        self.bit_array = bitarray.bitarray()
        for i in range(self.filter_len):
            self.bit_array.append(0)

    def hash1(self, str1):
        code = 0
        for i in str1:
            code = ((code * 17) + ord(i)) % self.filter_len
        return code

    def hash2(self, str1):
        code = 0
        for i in str1:
            code = ((code * 223) + ord(i)) % self.filter_len
        return code


    # Метод добавляет строку str1 в фильтр
    def add(self, str1):
        self.bit_array[self.hash1(str1)] = 1
        self.bit_array[self.hash2(str1)] = 1

    # Метод проверяет, имеется ли строка str1 в фильтре
    def is_value(self, str1):
        i1 = self.hash1(str1)
        i2 = self.hash2(str1)
        if self.bit_array[i1] == 1 and self.bit_array[i2] == 1:
            return True
        else:
            return False

"""bf = BloomFilter(32)
bf.add("0123456789")
print(bf.bit_array)
bf.add("1234567890")
print(bf.bit_array)
bf.add("2345678901")
print(bf.bit_array)
bf.add("3456789012")
print(bf.bit_array)
bf.add("4567890123")
print(bf.bit_array)
bf.add("5678901234")
print(bf.bit_array)
bf.add("6789012345")
print(bf.bit_array)
bf.add("7890123456")
print(bf.bit_array)
bf.add("8901234567")
print(bf.bit_array)
bf.add("9012345678")
print(bf.bit_array)
print(bf.is_value("5678901234"))"""