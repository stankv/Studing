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

    # Метод удаления одного узла (all=False)/всех узлов (all=True) по заданному значению
    def delete(self, val, all):
        node = self.head
        if self.len() == 0:    # если список пустой то ничего не делаем
            return
        elif self.len() == 1 and node.value == val:    # если в связанном списке только 1 узел обнуляем список
            self.head = None    
            self.tail = None
            return
        elif self.len() > 1:
            node = self.head
            while node is not None:    # "отсекаем голову" если там есть искомые значения
                if node.value == val:    # если заданное значение = значению 1-го узла
                    if node.next is not None:
                        self.head = node.next
                        node = node.next
                    else:
                        # удалить весь список
                        self.clean()
                        return
                else:
                    break
            # ищем узел внутри списка и удаляем его, если он есть (значение совпадает с заданным)
            #node = self.head
            while node is not None:
                new = node.next
                if node.next is None:
                    if node.value == val:
                        node = None
                    return
                else:
                    if node.next.value == val:
                        node.next = node.next.next
                        if not all:
                            return
                if node.next is None:
                    return
                if node.next.value != val:
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