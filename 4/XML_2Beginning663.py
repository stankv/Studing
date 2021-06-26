# Функция удаляет все узлы по заданному тегу в XML-документе.
import xml.etree.ElementTree as ETree
import os.path

my_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../4/data/demo1.xml')
xml1 = ETree.parse(my_path)
root = xml1.getroot()

def DelOfNodes(root_node, tag_name, path):
    success = False
    for item in root_node.iter():    # Идем по всем узлам документа
        if item.find(tag_name) != None:    # Если тег найден, то удаляем его
            for lng in item.findall(tag_name):
                item.remove(lng)
            success = True
    if success:    # Если тег был найден и удален, то перезаписываем файл
        serialze = ETree.tostring(root_node, encoding='utf8', method='xml').decode()
        fil = open(path, "w")  
        fil.write(serialze)