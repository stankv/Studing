# ФИЛЬТР БЛЮМА
# (входные данные - строки)

class BloomFilter:

    # создаём битовый массив длиной f_len
    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = 0

    def hash1(self, str1):
        code = 0
        for i in str1:
            code = ((code * 17) + ord(i)) % self.filter_len
        return 0 | (1 << code)

    def hash2(self, str1):
        code = 0
        for i in str1:
            code = ((code * 223) + ord(i)) % self.filter_len
        return 0 | (1 << code)


    # Метод добавляет строку str1 в фильтр
    def add(self, str1):
        self.filter |= self.hash1(str1)
        self.filter |= self.hash2(str1)
        return self.filter


    # Метод проверяет, имеется ли строка str1 в фильтре
    def is_value(self, str1):
        bitmask = self.filter & (self.hash1(str1) | self.hash2(str1))
        if bitmask == self.hash1(str1) | self.hash2(str1):
            return True
        return False