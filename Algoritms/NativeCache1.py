# РЕАЛИЗАЦИЯ КЭША (НА ОСНОВЕ ХЕШ-ТАБЛИЦЫ)

class NativeCache:
    def __init__(self, sz):
        self.size = sz                      # размер хэш-таблицы (желательно простое число)
        self.slots = [None] * self.size     # массив ключей
        self.values = [None] * self.size    # массив значений
        self.hits = [0] * self.size         # массив количества обращений к каждому ключу
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
                self.hits[index] += 1
                return True
        return False

    # Метод "удаления" из кэша элемента с минимальным количеством обращений
    def del_from_cache(self):
        index = self.hits.index(min(self.hits))    # возвращает индекс первого найденного элемента
        self.slots[index] = None
        self.values[index] = None
        self.hits[index] = 0
        return index

    # Метод записи в кэш пары ключ-значение
    def put(self, key, value):
        index = self.seek_slot(key)
        if index is not None:    # если есть свободное место или ключ key
            if self.slots[index] == key:    # если ключ key есть, то меняем его значение и засчитываем обращение к ключу
                self.values[index] = value
                self.hits[index] += 1
            else:    # ключа key нет, но есть свободный слот
                self.slots[index] = key
                self.values[index] = value
        else:    # если нет такого ключа или свободных слотов
            index = self.del_from_cache()    # "удаляем" элемент с наименьшим количеством обращений
            self.slots[index] = key
            self.values[index] = value

    # Метод поиска и извлечения значения по ключу (или None, если ключ не найден)
    def get(self, key):
        index = self.seek_slot(key)
        if index is not None and self.slots[index] == key:
            self.hits[index] += 1
            return self.values[index]
        return None