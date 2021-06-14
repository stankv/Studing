# Тестирование рекурсивной функции для XML_1Beginning533.py
import unittest
import xml.etree.ElementTree as ETree
import os.path
from XML_1Beginning533 import NumberOfNodes


class XML1_Test_533(unittest.TestCase):

    def setUp(self):
        xml1 = ETree.parse(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../4/data/demo.xml'))
        self.root = xml1.getroot()
        self.L = []

# РЕГРЕССИОННЫЕ ТЕСТЫ
# 1. Существующий атрибут
    def test_regression1_1(self):
        attr = "name"
        self.assertEqual(NumberOfNodes(attr, self.root, self.L), 7)
    
# 2. Несуществующий атрибут
    def test_regression1_2(self):
        attr = "name777"
        self.assertEqual(NumberOfNodes(attr, self.root, self.L), 0)

# 3. Пустой атрибут
    def test_regression1_3(self):
        attr = ""
        self.assertEqual(NumberOfNodes(attr, self.root, self.L), 0)

if __name__ == '__main__':
    unittest.main()