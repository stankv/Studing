# Тестирование функции для XML_2Beginning663.py
import unittest
import xml.etree.ElementTree as ETree
import os.path
from XML_2Beginning663 import DelOfNodes

class XML2_Test_663(unittest.TestCase):
    
    def setUp(self):
        self.my_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../4/data/demo1.xml')
        xml1 = ETree.parse(self.my_path)
        self.root = xml1.getroot()

    # Функция проверяет наличие тега во всей структуре документа
    def check(self, tag_name):
        for item in self.root.iter():
            if item.tag == tag_name:
                return True
        return False

# РЕГРЕССИОННЫЕ ТЕСТЫ
# 1. Удаляем теги нижнего (2-го) уровня и проверяем что они ВСЕ действительно удалены
    def test_regression1_1(self):
        tag_name = "language"    # их 3
        result1 = self.check(tag_name)    # проверяем что теги есть в документе - True
        DelOfNodes(self.root, tag_name, self.my_path)    # удаляем теги
        result2 = self.check(tag_name)    # проверяем что тегов больше нет в документе - False
        self.assertNotEqual(result1, result2)

# 2. Удаляем тег верхнего (1-го) уровня и проверяем что его вложенные теги удалены
    def test_regression2_1(self):
        tag_name = "pc_item"
        result1 = self.check(tag_name)
        DelOfNodes(self.root, 'pc', self.my_path)
        result2 = self.check(tag_name)
        self.assertNotEqual(result1, result2)

# 3. Удаляем теги верхнего (1-го) уровня
    def test_regression3_1(self):
        tag_name = "name"
        result1 = self.check(tag_name)
        DelOfNodes(self.root, tag_name, self.my_path)
        result2 = self.check(tag_name)
        self.assertNotEqual(result1, result2)

    def test_regression3_2(self):
        tag_name = "age"
        result1 = self.check(tag_name)
        DelOfNodes(self.root, tag_name, self.my_path)
        result2 = self.check(tag_name)
        self.assertNotEqual(result1, result2)

if __name__ == '__main__':
    unittest.main()