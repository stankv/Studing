# Тестирование функции вставки узла newNode после заданного узла afterNode - insert(afterNode, newNode)
import unittest
from LinkedList1 import Node, LinkedList

class insert_test(unittest.TestCase):

# РЕГРЕССИОННЫЕ ТЕСТЫ

# 1. Пустой связанный список
    def test_regression1(self):
        s_list = LinkedList()
        n1 = Node(10)
        s_list.insert(None, n1)
        self.assertEqual(s_list.find(10), n1)

# 2. Связанный список с 1 элементом
    def test_regression2(self):
        s_list = LinkedList()
        n1 = Node(10)
        n2 = Node(20)
        s_list.add_in_tail(n1)
        s_list.insert(n1, n2)
        L = []
        node = s_list.head
        while node is not None:
            L.append(node)
            node = node.next
        self.assertEqual(L, [n1, n2])

# 3. Вставка после 1-го элемента связанного списка
    def test_regression3(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        n_new = Node(100)
        s_list.insert(n1, n_new)
        L = []
        node = s_list.head
        while node is not None:
            L.append(node)
            node = node.next
        self.assertEqual(L, [n1, n_new, n2, n3])

# 4. Вставка перед последним элементом связанного списка
    def test_regression4(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        n_new = Node(100)
        s_list.insert(n2, n_new)
        L = []
        node = s_list.head
        while node is not None:
            L.append(node)
            node = node.next
        self.assertEqual(L, [n1, n2, n_new, n3])

if __name__ == '__main__':
    unittest.main()