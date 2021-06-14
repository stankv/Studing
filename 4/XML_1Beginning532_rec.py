# XML-документ: РЕКУРСИВНАЯ функция возвращает список всех значений (по всем узлам) для конкретного тега, если задано его название.
# Возвращает пустой список, если тег не найден.
# При вызове функции задавать аргумент List_values = []
import xml.etree.ElementTree as ETree
import os.path

xml1 = ETree.parse(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../4/data/demo.xml'))
root = xml1.getroot()

def ListValues(tag_name, root, List_values):
    for i in range(len(root)):
        if root[i].tag != tag_name and len(root[i]) == 0:
            continue
        elif root[i].tag == tag_name and len(root[i]) == 0:
            List_values.append(root[i].text)
        elif root[i].tag == tag_name and len(root[i]) > 0:
            level2 = root[i]
            for j in range(len(level2)):
                List_values.append(level2[j].text)
        elif root[i].tag != tag_name and len(root[i]) != 0:
            level2 = root[i]
            ListValues(tag_name, level2, List_values)
    return List_values