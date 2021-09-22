# РЕАЛИЗАЦИЯ УПОРЯДОЧЕННОГО СПИСКА (НА ОСНОВЕ ДВУНАПРАВЛЕННОГО СВЯЗАННОГО СПИСКА)
# (Для данной реализации значения узлов - числа)

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

    # Метод сравнения двух значений
    def compare(self, v1, v2):
        if v1 < v2:    # -1 если v1 < v2
            return -1
        elif v1 > v2:    # +1 если v1 > v2
            return 1
        elif v1 == v2:    # 0 если v1 == v2
            return 0

    # Метод добавления нового элемента по значению
    def add(self, value):
        node_new = Node(value)
        node = self.head
        length = self.len()    # вычисляем 1 раз чтобы не делать этого несколько раз в if-ах
        if length == 0:    # если список пустой
            self.head = node_new
            node_new.prev = None
            node_new.next = None
            self.tail = node_new
            return
        if self.__ascending:    # Если элементы упорядоченны по возрастанию
            if length == 1:    # если в списке только 1 элемент
                cmpr = self.compare(self.head.value, value)
                if cmpr == -1 or cmpr == 0:    # то добавляем в хвост
                    self.tail.next = node_new
                    node_new.prev = self.tail
                    self.tail = node_new
                    return
                elif cmpr == 1:    # то добавляем в голову
                    node_new.next = self.head
                    self.head.prev = node_new
                    self.head = node_new
                    return
            elif length > 1:    # если в списке больше чем 1 элемент
                cmpr = self.compare(self.head.value, value)
                if cmpr == 1 or cmpr == 0:    # если значение "головы" больше/равно value то добавляем в голову
                    node_new.next = self.head
                    self.head.prev = node_new
                    self.head = node_new
                    return
                node = self.head
                while node is not None:
                    if node.next is not None:    # если еще не добрались до последнего элемента
                        if self.compare(node.value, value) == -1 and (self.compare(value, node.next.value) == -1
                           or self.compare(value, node.next.value) == 0):
                            node_new.prev = node
                            node_new.next = node.next
                            node.next.prev = node_new
                            node.next = node_new
                            return
                        elif self.compare(node.value, value) == 0 and self.compare(value, node.next.value) == -1:
                            node_new.prev = node
                            node_new.next = node.next
                            node.next.prev = node_new
                            node.next = node_new
                            return
                    else:    # если добрались до последнего элемента
                        if self.compare(node.value, value) == -1 or self.compare(node.value, value) == 0: # то добавляем в хвост
                            self.tail.next = node_new
                            node_new.prev = self.tail
                            self.tail = node_new
                            return
                        elif self.compare(node.value, value) == 1:
                            return
                    node = node.next
        else:    # Если элементы упорядочены по убыванию
            if length == 1:    # если в списке только 1 элемент
                cmpr = self.compare(self.head.value, value)
                if cmpr == 1 or cmpr == 0:    # то добавляем в хвост
                    self.tail.next = node_new
                    node_new.prev = self.tail
                    self.tail = node_new
                    return
                elif cmpr == -1:    # то добавляем в голову
                    node_new.next = self.head
                    self.head.prev = node_new
                    self.head = node_new
                    return
            elif length > 1:    # если в списке больше чем 1 элемент
                cmpr = self.compare(self.head.value, value)
                if cmpr == -1 or cmpr == 0:    # если значение "головы" меньше/равно value то добавляем в голову
                    node_new.next = self.head
                    self.head.prev = node_new
                    self.head = node_new
                    return
                node = self.head
                while node is not None:
                    if node.next is not None:    # если еще не добрались до последнего элемента
                        if self.compare(node.value, value) == 1 and (self.compare(value, node.next.value) == 1
                           or self.compare(value, node.next.value) == 0):
                            node_new.prev = node
                            node_new.next = node.next
                            node.next.prev = node_new
                            node.next = node_new
                            return
                        elif self.compare(node.value, value) == 0 and self.compare(value, node.next.value) == 1:
                            node_new.prev = node
                            node_new.next = node.next
                            node.next.prev = node_new
                            node.next = node_new
                            return
                    else:    # если добрались до последнего элемента
                        if self.compare(node.value, value) == 1 or self.compare(node.value, value) == 0: # то добавляем в хвост
                            self.tail.next = node_new
                            node_new.prev = self.tail
                            self.tail = node_new
                            return
                        elif self.compare(node.value, value) == -1:
                            return
                    node = node.next
        return

    # Метод поиска узла по заданному значению
    def find(self, val):
        node = self.head
        if self.__ascending:    # если элементы массива по возрастанию
            while node is not None:
                if node.value == val:
                    return node
                if node.prev.value < val and node.next.value > val:
                    return None
                node = node.next
        else:    # если элементы массива по убыванию
            while node is not None:
                if node.value == val:
                    return node
                if node.prev.value > val and node.next.value < val:
                    return None
                node = node.next
        return None

    # Метод удаления узла по его значению
    def delete(self, val):
        k = self.len()    # вычисляем длину списка 1 раз, чтобы не делать этого каждый раз дальше
        node = self.head
        if k == 0:    # если список пустой то ничего не делаем
            return
        elif k == 1 and node.value == val:    # если всего 1 узел и его значение = val, то обнуляем список
            self.head = None    
            self.tail = None
            return
        elif k > 1:    # если в списке несколько узлов
            while node is not None:
                if self.head.value == val:    # если первый узел равен искомому (удаляемому)
                    self.head = node.next
                    self.head.prev = None
                    return
                elif self.head.value != val:
                    if node.value == val and node.next is not None:
                        last = node.next
                        node.prev.next = node.next
                        node.next.prev = node.prev
                        return
                    elif node.value == val and node.next is None:
                        node.prev.next = None
                        self.tail = node.prev
                        return
                node = node.next
        return

    # Метод очистки списка
    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    # Метод вычисления текущей длины списка
    def len(self):
        node = self.head
        if node is not None:
            count = 0
            while node is not None:
                count += 1
                node = node.next
            return count
        return 0

    # Метод возвращает список всех узлов упорядоченного списка
    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

# Наследник OrderedList для упорядоченного хранения строк
class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):    # переопределённая версия для строк
        v1 = v1.strip()    # удаляем из сравниваемых строк начальные и конечные пробелы
        v2 = v2.strip()
        if v1 < v2:      # -1 если v1 < v2
            return -1
        elif v1 > v2:    # +1 если v1 > v2
            return 1
        elif v1 == v2:   # 0 если v1 == v2
            return 0