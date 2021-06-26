# Тестирование функции для XML_2Beginning662.py
import unittest
import xml.etree.ElementTree as ETree
import os.path
from XML_2Beginning662 import ParentOfNode

class XML2_Test_662(unittest.TestCase):
    
    def setUp(self):
        xml1 = ETree.parse(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../4/data/demo.xml'))
        self.root = xml1.getroot()

# РЕГРЕССИОННЫЕ ТЕСТЫ
# 1. Теги 1-го уровня, для них всех родитель - корневой узел 'data'
    def test_regression1_1(self):
        tag_name = "name"
        self.assertEqual(ParentOfNode(self.root, tag_name), self.root)

    def test_regression1_2(self):
        tag_name = "age"
        self.assertEqual(ParentOfNode(self.root, tag_name), self.root)

    def test_regression1_3(self):
        tag_name = "sex"
        self.assertEqual(ParentOfNode(self.root, tag_name), self.root)

    def test_regression1_4(self):
        tag_name = "languages"
        self.assertEqual(ParentOfNode(self.root, tag_name), self.root)

    def test_regression1_5(self):
        tag_name = "pc"
        self.assertEqual(ParentOfNode(self.root, tag_name), self.root)

# 2. Теги 2-го уровня
    def test_regression2_1(self):
        tag_name = "language"    # родитель - 'languages'
        self.assertEqual(ParentOfNode(self.root, tag_name), self.root.find('languages'))

    def test_regression2_2(self):
        tag_name = "pc_item"    # родитель - 'pc'
        self.assertEqual(ParentOfNode(self.root, tag_name), self.root.find('pc'))

# 3. Отсутствующий тег
    def test_regression3_1(self):
        tag_name = "noname1"
        self.assertEqual(ParentOfNode(self.root, tag_name), None)

# 4. Пустой тег
    def test_regression4_1(self):
        tag_name = ""
        self.assertEqual(ParentOfNode(self.root, tag_name), None)

# 5. Корневой узел (родителя не имеет)
    def test_regression5_1(self):
        tag_name = "data"
        self.assertEqual(ParentOfNode(self.root, tag_name), None)

if __name__ == '__main__':
    unittest.main()