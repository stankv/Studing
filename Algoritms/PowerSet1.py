# РЕАЛИЗАЦИЯ МНОЖЕСТВА НА ОСНОВЕ СПИСКА
# (каждое значение хранится в нём в единичном экземпляре)
class PowerSet:

    def __init__(self):
        self.my_set = []     # массив элементов множества

    # Метод вычисления количества элементов в множестве
    def size(self):
        return len(self.my_set)

    # Метод записи значения в множество
    def put(self, value):
        if not self.get(value):
            self.my_set.append(value)


    # Метод поиска значения в множестве
    def get(self, value):    # возвращает True если value имеется в множестве, иначе False
        if value in self.my_set:
            return True
        return False

    # Метод удаления значения из множества
    def remove(self, value):    # возвращает True если value удалено, иначе False
        if self.get(value):
            self.my_set.remove(value)
            return True
        return False

    # Метод возвращает пересечение текущего множества и set2
    # (т.е. множество, в котором есть только те элементы, которые имеются в каждом из множеств)
    def intersection(self, set2):
        result = PowerSet()
        for i in self.my_set:
            if set2.get(i):
                result.put(i)
        return result

    # Метод возвращает объединение текущего множества и set2
    # (т.е. множество, в котором есть все элементы из каждого множества)
    def union(self, set2):
        result = PowerSet()
        for i in self.my_set:
            result.put(i)
        for i in set2.my_set:
            if not self.get(i):
                result.put(i)
        return result

    # Метод возвращает разницу текущего множества и set2
    # (т.е. подмножество текущего множества из таких элементов, которые не входят в множество-параметр)
    def difference(self, set2):
        result = PowerSet()
        for i in self.my_set:
            if not set2.get(i):
                result.put(i)
        return result

    # Метод возвращает True, если set2 есть подмножество текущего множества, иначе False
    def issubset(self, set2):
        for i in set2.my_set:
            if not self.get(i):
                return False
        return True