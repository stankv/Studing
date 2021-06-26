# Функция находит родителя заданного (по имени тега) узла, и возвращает его (тип Element).
# Если не находит, то возвращает None.
import xml.etree.ElementTree as ETree
import os.path

xml1 = ETree.parse(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../4/data/demo.xml'))
root = xml1.getroot()

def ParentOfNode(root_node, tag_name):    # рекурсивная функция!
    if root_node.find(tag_name) != None:
        return root_node
    else:
        for item in root_node:
            if len(item) > 0:
                if item.find(tag_name) != None:
                    return item
                else:
                    ParentOfNode(item, tag_name)