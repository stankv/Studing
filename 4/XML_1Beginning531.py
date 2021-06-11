# Чтение XML-файла (2 уровня вложенности) и вывод на консоль содержания узлов документа:
# названия тегов, их атрибуты и значения.
import xml.etree.ElementTree as ETree
import os.path

xml1 = ETree.parse(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../4/data/demo.xml'))
root = xml1.getroot()

for i in range(len(root)):
    if len(root[i]) == 0:     # 1-й уровень
        print(root[i].tag, root[i].text)
    elif len(root[i]) > 0:    # 2-й уровень
        print("  ", root[i].tag)
        level2 = root[i]
        for j in range(len(level2)):
            print("    ", level2[j].tag, level2[j].get("name"), level2[j].text)