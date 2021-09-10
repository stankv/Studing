# Тестирование функции удаления одного узла (all=False)/всех узлов (all=True) 
# по заданному значению - delete(val, all) для двусвязного списка
import unittest
from LinkedList2 import Node, LinkedList2

class delete_test(unittest.TestCase):

# РЕГРЕССИОННЫЕ ТЕСТЫ

# 1. Пустой связанный список, all=False
    def test_regression1(self):
        s_list = LinkedList2()
        n1 = Node(10)
        s_list.delete(10)
        L = node_list(s_list)
        self.assertEqual(L, [])

# 2. Пустой связанный список, all=True
    def test_regression2(self):
        s_list = LinkedList2()
        n1 = Node(10)
        s_list.delete(10, True)
        L = node_list(s_list)
        self.assertEqual(L, [])

# 3. Cвязанный список c 1 элементом, all=False
    def test_regression3(self):
        s_list = LinkedList2()
        n1 = Node(10)
        s_list.add_in_tail(n1)
        s_list.delete(10)
        L = node_list(s_list)
        self.assertEqual(L, [])

# 4. Cвязанный список c 1 элементом, all=True
    def test_regression4(self):
        s_list = LinkedList2()
        n1 = Node(10)
        s_list.add_in_tail(n1)
        s_list.delete(10, True)
        L = node_list(s_list)
        self.assertEqual(L, [])

# 5. Cвязанный список, удаление первого элемента, all=False
    def test_regression5(self):
        s_list = LinkedList2()
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.delete(10)
        L = node_list(s_list)
        self.assertEqual(L, [n2,n3])

# 6. Cвязанный список, удаление последнего элемента, all=False
    def test_regression6(self):
        s_list = LinkedList2()
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.delete(30)
        L = node_list(s_list)
        self.assertEqual(L, [n1,n2])

# 7. Cвязанный список, удаление предпоследнего элемента, all=False
    def test_regression7(self):
        s_list = LinkedList2()
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        n4 = Node(40)
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)
        s_list.delete(30)
        L = node_list(s_list)
        self.assertEqual(L, [n1,n2,n4])

# 8. Cвязанный список, удаление всех одинаковых элементов, all=True
    def test_regression8(self):
        s_list = LinkedList2()
        n1 = Node(10)
        n2 = Node(10)
        n3 = Node(30)
        n4 = Node(40)
        n5 = Node(10)
        n6 = Node(40)
        n7 = Node(10)
        n8 = Node(40)
        n9 = Node(10)
        n10 = Node(10)
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)
        s_list.add_in_tail(n5)
        s_list.add_in_tail(n6)
        s_list.add_in_tail(n7)
        s_list.add_in_tail(n8)
        s_list.add_in_tail(n9)
        s_list.add_in_tail(n10)
        s_list.delete(10, True)
        L = node_list(s_list)
        self.assertEqual(L, [n3,n4,n6,n8])

# 9. Cвязанный список, удаление всех одинаковых элементов подряд в середине, all=True
    def test_regression9(self):
        s_list = LinkedList2()
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        n4 = Node(40)
        n5 = Node(40)
        n6 = Node(40)
        n7 = Node(40)
        n8 = Node(40)
        n9 = Node(90)
        n10 = Node(100)
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(n3)
        s_list.add_in_tail(n4)
        s_list.add_in_tail(n5)
        s_list.add_in_tail(n6)
        s_list.add_in_tail(n7)
        s_list.add_in_tail(n8)
        s_list.add_in_tail(n9)
        s_list.add_in_tail(n10)
        s_list.delete(40, True)
        L = node_list(s_list)
        self.assertEqual(L, [n1,n2,n3,n9,n10])

# Ф-я формирования массива узлов после применения удаления
def node_list(s_list):
    S = []
    node = s_list.head
    while node is not None:
        S.append(node)
        node = node.next
    return S

if __name__ == '__main__':
    unittest.main()