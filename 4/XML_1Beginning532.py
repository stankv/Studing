# XML-документ: Функция возвращает список всех значений (по всем узлам) для конкретного тега, если задано его название.
# Возвращает пустой список, если тег не найден.
import xml.etree.ElementTree as ETree
import os.path

xml1 = ETree.parse(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../4/data/demo.xml'))
root = xml1.getroot()

List_values = []
def ListValues(tag_name):
    for i in range(len(root)):
        if len(root[i]) == 0 and root[i].tag == tag_name:
            List_values.append(root[i].text)
            return List_values
        elif len(root[i]) > 0 and root[i].tag == tag_name:
            level_down = root[i]
            for j in range(len(level_down)):
                List_values.append(level_down[j].text)
            return List_values
        elif len(root[i]) > 0 and root[i].tag != tag_name:
            level_down = root[i]
            k = False
            for j in range(len(level_down)):
                if level_down[j].tag == tag_name:
                    List_values.append(level_down[j].text)
                    k = True
            if k:
                return List_values
    return List_values
