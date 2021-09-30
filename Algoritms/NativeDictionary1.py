# РЕАЛИЗАЦИЯ АССОЦИАТИВНОГО МАССИВА (СЛОВАРЯ) НА ОСНОВЕ ХЕШ-ТАБЛИЦЫ
# Считаем, что размер массива фиксирован и гарантированно не будет превышен при применении.
class NativeDictionary:
    def __init__(self, sz):
        self.size = sz                      # # размер хэш-таблицы (желательно простое число)
        self.slots = [None] * self.size     # массив ключей
        self.values = [None] * self.size    # массив значений
        self.step = 3    # длина шага (количество слотов) для поиска следующего свободного слота

    # Метод по входному значению возвращает индекс слота
    def hash_fun(self, key):    # в качестве key поступают строки!
        key = str(key).strip()    # если вдруг число, то приводим к строке и удаляем пробелы слева и справа
        sum = 0
        for i in key:
            sum += ord(i)
        return sum % self.size

    # Метод поиска слота (по входному значению сначала рассчитывает индекс хэш-функцией, а затем отыскивает подходящий
    # слот для него с учётом коллизий, или возвращает None, если это не удалось)
    def seek_slot(self, key):
        index = self.hash_fun(key)
        count = 0
        while count <= self.size - 1:
            if self.slots[index] is None or self.slots[index] == key:
                return index
            if (index + self.step) > (self.size - 1):
                index = self.size - (index + self.step)
            else:
                index += self.step
            count += 1
        return None

    # Метод проверки, имеется ли в слотах такой ключ
    def is_key(self, key):    # возвращает True если ключ имеется, иначе False
        index = self.seek_slot(key)
        if index is not None:
            if self.slots[index] == key:
                return True
        return False

    # Метод записи в словарь пары ключ-значение
    def put(self, key, value):
        index = self.seek_slot(key)
        if index is not None:
            self.slots[index] = key
            self.values[index] = value

    # Метод поиска и извлечения значения по ключу (или None, если ключ не найден)
    def get(self, key):
        index = self.seek_slot(key)
        if index is not None:
            return self.values[index]
        return None