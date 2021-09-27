# РЕАЛИЗАЦИЯ ХЭШ-ТАБЛИЦЫ
# в качестве value поступают строки!
# Для разрешения коллизий используется метод последовательных проб
class HashTable:
    def __init__(self, sz, stp):
        self.size = sz     # размер хэш-таблицы (желательно простое число)
        self.step = stp    # длина шага (количество слотов) для поиска следующего свободного слота
        self.slots = [None] * self.size

     # Метод по входному значению вычисляет индекс слота
    def hash_fun(self, value):        # в качестве value поступают строки!
        value = str(value).strip()    # если вдруг число, то приводим к строке и удаляем пробелы слева и справа
        sum = 0
        for i in value:
            sum += ord(i)
        return sum % self.size

    # Метод поиска слота (по входному значению сначала рассчитывает индекс хэш-функцией, а затем отыскивает подходящий
    # слот для него с учётом коллизий, или возвращает None, если это не удалось)
    def seek_slot(self, value):
        index = self.hash_fun(value)
        count = 0
        while count <= self.size - 1:
            if self.slots[index] is None:
                return index
            if (index + self.step) > (self.size - 1):
                index = self.size - (index + self.step)
            else:
                index += self.step
            count += 1
        return None

    # Метод помещает значение value в слот, вычисляемый с помощью функции поиска
    # (возвращается индекс слота или None, если из-за коллизий элемент не удаётся разместить)
    def put(self, value):
        value = str(value).strip()
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value
            return index
        else:
            return None

    # Метод проверяет, имеется ли в слотах указанное значение, и возвращает либо индекс слота, либо None
    def find(self, value):
        value = str(value).strip()
        index = self.hash_fun(value)
        count = 0
        while count <= self.size - 1:
            if self.slots[index] == value:
                return index
            if (index + self.step) > (self.size - 1):
                index = self.size - (index + self.step)
            else:
                index += self.step
            count += 1
        return None