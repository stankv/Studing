# Тестирование функции для XML_2Beginning661.py
import unittest
import xml.etree.ElementTree as ETree
import os.path
from XML_2Beginning661 import ListOfNodes

class XML2_Test_661(unittest.TestCase):
    
    def setUp(self):
        xml1 = ETree.parse(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../4/data/demo.xml'))
        self.root = xml1.getroot()

# РЕГРЕССИОННЫЕ ТЕСТЫ
# 1. Теги 1-го уровня
    def test_regression1_1(self):
        tag_name = "name"
        self.assertEqual(ListOfNodes(self.root, tag_name), ['name'])

    def test_regression1_2(self):
        tag_name = "age"
        self.assertEqual(ListOfNodes(self.root, tag_name), ['age'])

    def test_regression1_3(self):
        tag_name = "sex"
        self.assertEqual(ListOfNodes(self.root, tag_name), ['sex'])

    def test_regression1_4(self):
        tag_name = "languages"
        result = ['languages', 'language', 'language', 'language']
        self.assertEqual(ListOfNodes(self.root, tag_name), result)

    def test_regression1_5(self):
        tag_name = "pc"
        result = ['pc', 'pc_item', 'pc_item', 'pc_item', 'pc_item']
        self.assertEqual(ListOfNodes(self.root, tag_name), result)
        
# 2. Теги 2-го уровня
    def test_regression2_4(self):
        tag_name = "language"
        result = ['language', 'language', 'language']
        self.assertEqual(ListOfNodes(self.root, tag_name), result)

    def test_regression2_5(self):
        tag_name = "pc_item"
        result = ['pc_item', 'pc_item', 'pc_item', 'pc_item']
        self.assertEqual(ListOfNodes(self.root, tag_name), result)

# 3. Отсутствующий тег
    def test_regression3_1(self):
        tag_name = "noname1"
        self.assertEqual(ListOfNodes(self.root, tag_name), [])

# 4. Пустой тег
    def test_regression4_1(self):
        tag_name = ""
        self.assertEqual(ListOfNodes(self.root, tag_name), [])

# 5. Корневой узел
    def test_regression5_1(self):
        tag_name = "data"
        result = ['data', 'name', 'age', 'sex', 'languages', 'language', 'language', 'language', 'pc', 'pc_item', 'pc_item', 'pc_item', 'pc_item']
        self.assertEqual(ListOfNodes(self.root, tag_name), result)

if __name__ == '__main__':
    unittest.main()