# Время жизни переменных

# 1-5. Рассматриваем код решения задачи "Делаем национальный редактор "Лапоть"" курса "28 задач"
# https://github.com/stankv/Studing/blob/main/20_BastShoe.py
# Это единственная в курсе задача, в которой для решения пришлось применить глобальные переменные:
# глобальные переменные
S = []    # массив получившихся строк
current_stroka = ""    # текущая строка
index_S = -1   # индекс текущей строки в массиве
flag = False

def BastShoe(command):
    global S
    global current_stroka
    global index_S
    global flag
# 1-4. Сужаем область видимости этих переменных за счет помещения их в класс:
class main_variables:
    def __init__(self):
        self.S = []
        self.current_stroka = ""
        self.index_S = -1
        self.flag = False
# 5. Можно еще более сузить область видимости этих переменных, сделав их приватными, но тогда придется увеличить
# "количество" кода, написав для обращения к ним геттеры и сеттеры.

# 6-10. Рассматриваем код решения задачи "Упорядоченный список (на основе двунаправленного связанного списка" 
# курса "Алгоритмы и структуры данных 1" - https://github.com/stankv/Studing/blob/main/Algoritms/OrderedList1.py
# Задаем узел
class Node:
    def __init__(self, v):
        self.value = v      # значение узла
        self.prev = None    # указатель на предыдущий узел
        self.next = None    # указатель на следующий узел

# Задаем упорядоченный список
class OrderedList:
    def __init__(self, asc):    # Инициализация упорядоченного списка
        self.head = None        # указатель на узел-голову списка
        self.tail = None        # указатель на завершающий узел
        self.__ascending = asc  # определяет по возрастанию (True) или по убыванию (False) значений хранятся узлы

# Все переменные в конструкторах этих классов можно сделать приватными:
class Node:
    def __init__(self, v):
        self.__value = v
        self.__prev = None
        self.__next = None

class OrderedList:
    def __init__(self, asc):
        self.__head = None
        self.__tail = None
        self.__ascending = asc

# 11-15. Рассматриваем код решения задачи "Кэш (на основе хэш-таблицы)" курса "Алгоритмы и структуры данных 1"
# https://github.com/stankv/Studing/blob/main/Algoritms/NativeCache1.py
class NativeCache:
    def __init__(self, sz):
        self.size = sz                      # размер хэш-таблицы (желательно простое число)
        self.slots = [None] * self.size     # массив ключей
        self.values = [None] * self.size    # массив значений
        self.hits = [0] * self.size         # массив количества обращений к каждому ключу
        self.step = 3    # длина шага (количество слотов) для поиска следующего свободного слота

# Аналогично предыдущему примеру, все переменные конструктора класса можно сделать приватными:
class NativeCache:
    def __init__(self, sz):
        self.__size = sz
        self.__slots = [None] * self.__size
        self.__values = [None] * self.__size
        self.__hits = [0] * self.__size
        self.__step = 3