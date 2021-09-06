# ОДНОНАПРАВЛЕННЫЙ СВЯЗАННЫЙ СПИСОК

# Определение узла
class Node:
    def __init__(self, v):
        self.value = v      # данное
        self.next = None    # связь, т.е. указатель на следующее значение

# Задаем связанный список
class LinkedList:
    def __init__(self):
        self.head = None    # указатель на узел-голову списка
        self.tail = None    # указатель на завершающий узел

    # Метод добавления нового узла в конец связанного списка
    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    # Метод отладочного вывода связанного списка
    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    # Метод поиска узла по заданному значению
    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    # Метод поиска всех узлов по конкретному значению
    def find_all(self, val):
        S = []
        node = self.head
        while node is not None:
            if node.value == val:
                S.append(node)
            node = node.next
        return S

    

    def delete(self, val, all=False):
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
                if self.head.value == val:
                    if node.next is None:
                        self.head = None
                        self.tail = None
                        return
                    self.head = node.next
                    if not all:
                        return
                else:
                    if node.next is None:
                        if node.value == val:
                            self.tail = last
                            node = None
                            last.next = None
                            return
                        self.tail = node
                        return
                    elif node.value == val and node.next.value != val and node.next.next is not None:
                        last.next = node.next
                    elif node.value == val and node.next.value == val and node.next.next is not None:
                        last.next = node.next.next
                    elif node.value == val and node.next.value == val and node.next.next is None:
                        self.tail = last
                        node = None
                        last.next = None
                        return
                    elif node.next.value == val and node.next.next is None:
                        node.next = None
                        self.tail = node
                        return
                    elif node.next.value == val and node.next.next is not None:
                        node.next = node.next.next
                        if not all:
                            return
                if node.value != val:
                    last = node
                node = node.next
            return


    # Метод очистки всего содержимого (создание пустого списка)
    def clean(self):
        self.head = None    
        self.tail = None

    # Метод вычисления текущей длины списка
    def len(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    # Метод вставки узла newNode после заданного узла afterNode
    def insert(self, afterNode, newNode):
        if self.len() == 0 or self.len() == 1:    # если список пустой или содержит только 1 узел
            self.add_in_tail(newNode)
        elif self.len() > 1 and self.tail != afterNode:    # длина списка > 1 и afterNode  не в конце списка
            node = self.head
            while node is not None:
                if node == afterNode:
                    old = node.next
                    node.next = newNode
                    newNode.next = old
                node = node.next
        elif self.len() > 1 and self.tail == afterNode:    # длина списка > 1 и afterNode в конце списка
            self.add_in_tail(newNode)