# Тестирование функции вставки узла самым первым элементом add_in_head(newNode)
import unittest
from LinkedList2 import Node, LinkedList2

class add_in_head_test(unittest.TestCase):

# РЕГРЕССИОННЫЕ ТЕСТЫ

# 1. Пустой связанный список
    def test_regression1(self):
        s_list = LinkedList2()
        n1 = Node(10)
        s_list.add_in_head(n1)
        self.assertEqual(s_list.head, n1)

# 2. Связанный список с 1 элементом
    def test_regression2(self):
        n1 = Node(10)
        s_list = LinkedList2()
        s_list.add_in_tail(n1)
        n2 = Node(20)
        s_list.add_in_head(n2)
        self.assertEqual(s_list.head, n2)

# 3. Связанный список с несколькими элементами
    def test_regression3(self):
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        n4 = Node(40)
        n5 = Node(50)
        s_list = LinkedList2()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)
        s_list.add_in_tail(n5)
        n0 = Node(100)
        s_list.add_in_head(n0)
        self.assertEqual(s_list.head, n0)

if __name__ == '__main__':
    unittest.main()