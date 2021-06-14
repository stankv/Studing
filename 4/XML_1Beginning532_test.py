# Тестирование функций для XML_1Beginning532.py и XML_1Beginning532_rec.py
import unittest
import xml.etree.ElementTree as ETree
import os.path
from XML_1Beginning532_rec import ListValues

xml1 = ETree.parse(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../4/data/demo.xml'))
root = xml1.getroot()

class XML1_Test_532(unittest.TestCase):

# РЕГРЕССИОННЫЕ ТЕСТЫ
# 1. Теги 1-го уровня
    def test_regression1_1(self):
        tag_name = "name"
        List_values = []
        self.assertEqual(ListValues(tag_name, root, List_values), ["Petya"])

    def test_regression1_2(self):
        tag_name = "age"
        List_values = []
        self.assertEqual(ListValues(tag_name, root, List_values), ['23'])

    def test_regression1_3(self):
        tag_name = "sex"
        List_values = []
        self.assertTrue(ListValues(tag_name, root, List_values))

    def test_regression1_4(self):
        tag_name = "languages"
        List_values = []
        result = ['9', '7', '8']
        self.assertEqual(ListValues(tag_name, root, List_values), result)

    def test_regression1_5(self):
        tag_name = "pc"
        List_values = []
        result = ['Linux', 'Intel Core i7-8700', '64', '5000']
        self.assertEqual(ListValues(tag_name, root, List_values), result)
        
# 2. Теги 2-го уровня
    def test_regression2_4(self):
        tag_name = "language"
        List_values = []
        result = ['9', '7', '8']
        self.assertEqual(ListValues(tag_name, root, List_values), result)

    def test_regression2_5(self):
        tag_name = "pc_item"
        List_values = []
        result = ['Linux', 'Intel Core i7-8700', '64', '5000']
        self.assertEqual(ListValues(tag_name, root, List_values), result)

# 3. Отсутствующий тег
    def test_regression3_1(self):
        tag_name = "noname1"
        List_values = []
        self.assertEqual(ListValues(tag_name, root, List_values), [])

# 4. Пустой тег
    def test_regression3_2(self):
        tag_name = ""
        List_values = []
        self.assertEqual(ListValues(tag_name, root, List_values), [])


if __name__ == '__main__':
    unittest.main()