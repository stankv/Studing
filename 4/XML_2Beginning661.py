# Функция формирует список всех узлов по заданному тегу в XML-документе. На вход функция получает корневой узел и тег.
import xml.etree.ElementTree as ETree
import os.path

xml1 = ETree.parse(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../4/data/demo.xml'))
root = xml1.getroot()

def ListOfNodes(root_node, tag_name):
    List_values =[]
    # ищем в документе теги с заданным именем
    for item in root_node.iter():
        if item.tag != tag_name:
            continue
        elif item.tag == tag_name and len(item) == 0:     # тег не имеет дочерних тегов
            List_values.append(item.tag)
        elif item.tag == tag_name and len(item) > 0:    # тег имеет дочерние теги
            for subitem in item.iter():
                List_values.append(subitem.tag)
    return List_values