# ДВУНАПРАВЛЕННЫЙ СВЯЗАННЫЙ СПИСОК

# Определение узла
from typing import NewType


class Node:
    def __init__(self, v):
        self.value = v      # значение узла
        self.prev = None    # указатель на предыдущий узел
        self.next = None    # указатель на следующий узел

# Задаем двунаправленный связанный список
class LinkedList2:  
    def __init__(self):     # Инициализация двусвязного списка
        self.head = None    # указатель на узел-голову списка
        self.tail = None    # указатель на завершающий узел

    # Метод добавления нового узла в конец связанного списка
    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    # 1. Метод поиска узла по заданному значению
    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    # 2. Метод поиска всех узлов по конкретному значению
    def find_all(self, val):
        S = []
        node = self.head
        while node is not None:
            if node.value == val:
                S.append(node)
            node = node.next
        return S

    # 3. Метод удаления одного узла (all=False) / всех узлов (all=True) по заданному значению
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
                if self.head.value == val:    # если первый узел равен искомому (удаляемому)
                    self.head = node.next
                    self.head.prev = None
                    if not all:
                        return
                    node = self.head
                    continue    # если голова списка состоит из нескольких удаляемых узлов, то повторяем
                elif self.head.value != val:
                    if node.value == val and node.next is not None:
                        last = node.next
                        node.prev.next = node.next
                        node.next.prev = node.prev
                        if not all:
                            return
                        node = last
                        continue
                    elif node.value == val and node.next is None:
                        node.prev.next = None
                        self.tail = node.prev
                        return
                node = node.next
        return

    # 4. Метод очистки всего содержимого (создание пустого списка)
    def clean(self):
        self.head = None
        self.tail = None

    # 5. Метод вычисления текущей длины списка
    def len(self):
        node = self.head
        if node is not None:
            count = 0
            while node is not None:
                count += 1
                node = node.next
            return count
        return 0

    # 6. Метод вставки узла newNode после заданного узла afterNode
    def insert(self, afterNode, newNode):
        length = self.len()    # вычисляем 1 раз чтобы не делать этого несколько раз в if-ах
        if afterNode == None and self.head is None:    # если список пустой и afterNode=None
            self.head = newNode
            return
        elif afterNode == None and self.head is not None:    # если список не пустой и afterNode=None
            self.add_in_tail(newNode)
        elif afterNode != None and self.head is None:    # список пустой, но введен afterNode
            return
        elif length == 1 and self.head == afterNode:    # список из 1 узла и он = afterNode
            self.add_in_tail(newNode)
            return
        elif length > 1 and self.tail == afterNode:    # эта проверка позволяет не проходить цикл по всем узлам как ниже
            self.add_in_tail(newNode)
            return
        elif length > 1:
            node = self.head
            while node is not None:
                if node == afterNode:
                    newNode.prev = node
                    newNode.next = node.next
                    node.next.prev = newNode
                    node.next = newNode
                    return
                node = node.next
        return

    # 7. Метод вставки узла самым первым элементом
    def add_in_head(self, newNode):
        if self.head is None:    # если список пустой
            self.head = newNode
            return
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        return

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next