# Тестирование рекурсивной функции для XML_1Beginning533.py
import unittest
import xml.etree.ElementTree as ETree
import os.path
from XML_1Beginning533 import NumberOfNodes

xml1 = ETree.parse(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../4/data/demo.xml'))
root = xml1.getroot()

class XML1_Test_533(unittest.TestCase):

# РЕГРЕССИОННЫЕ ТЕСТЫ
# 1. Существующий атрибут
    def test_regression1_1(self):
        attr = "name"
        L = []
        self.assertEqual(NumberOfNodes(attr, root, L), 7)
    
# 2. Несуществующий атрибут
    def test_regression1_2(self):
        attr = "name777"
        L = []
        self.assertEqual(NumberOfNodes(attr, root, L), 0)

# 3. Пустой атрибут
    def test_regression1_3(self):
        attr = ""
        L = []
        self.assertEqual(NumberOfNodes(attr, root, L), 0)

if __name__ == '__main__':
    unittest.main()