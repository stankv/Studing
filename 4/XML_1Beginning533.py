# XML-документ: РЕКУРСИВНАЯ функция, возвращает количество узлов в документе, включая дочерние, оснащённые заданным атрибутом. 
# При вызове функции задавать аргумент L = []
import xml.etree.ElementTree as ETree
import os.path

xml1 = ETree.parse(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../4/data/demo.xml'))
root = xml1.getroot()

def NumberOfNodes(attr, root, L):
    for i in range(len(root)):
        if attr in root[i].attrib.keys() and len(root[i]) == 0:
            L.append(1)
        elif attr in root[i].attrib.keys() and len(root[i]) > 0:
            L.append(1)
            level2 = root[i]
            NumberOfNodes(attr, level2, L)
        elif not attr in root[i].attrib.keys() and len(root[i]) > 0:
            level2 = root[i]
            NumberOfNodes(attr, level2, L)
    return sum(L)