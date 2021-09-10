# Тестирование функции очистки всего содержимого двусвязанного списка clean()
import unittest
from LinkedList2 import Node, LinkedList2
import random

class clean_test(unittest.TestCase):

# РЕГРЕССИОННЫЕ ТЕСТЫ

# 1. Пустой связанный список
    def test_regression1(self):
        s_list = LinkedList2()
        self.assertEqual(s_list.clean(), None)

# 2. Связанный список с одним узлом
    def test_regression2(self):
        n1 = Node(10)
        s_list = LinkedList2()
        s_list.add_in_tail(n1)
        self.assertEqual(s_list.clean(), None)

# 3. Связанный список со случайным количеством узлов
    def test_regression3(self):
        s_list = LinkedList2()
        for i in range(random.randint(1, 1000)):
            s_list.add_in_tail(Node(i))
        self.assertEqual(s_list.clean(), None)

if __name__ == '__main__':
    unittest.main()