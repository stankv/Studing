# КОНВЕРТИРУЕТ ГРАФИЧЕСКИЕ ФАЙЛЫ ЗАДАННОГО КАТАЛОГА В ДРУГОЙ ФОРМАТ

import os.path
import string
from PIL import Image

def my_tree(my_path, my_flag):
    list_file = []
    if not os.path.isdir(my_path):    #  проверка существования каталога
        success = False
    else:
        success = True
        for root, dirs, files in os.walk(my_path):
            # Текущий каталог в рут. перебираем подкаталоги из списка files 
            for file in files:
                list_file.append(root + '\\' + file)
            if not my_flag:  # Тут по флагу проверка, если ЛОЖЬ, то один проход цикла и выход
                return (list_file, success)
        return (list_file, success)
    return (list_file, success)   

def convert(extension1, extension2):
    # создаем список файлов текущего каталога
    F, Success = my_tree(path1, flag)
    if not Success:
        return (0, 0)    # каталог не найден
    if len(F) == 0:
        return (1, 0)    # в текущем каталоге нет никаких файлов
    # ищем в списке файлов те, что с нужным расширением
    str1 = '.' + extension1
    count = 0    # счетчик нужных файлов
    for ani in F:
        Path_file = os.path.split(ani)
        if Path_file[1].find(str1) >= 0:
            im = Image.open(ani)
            S = Path_file[1].split('.')
            str2 = S[0] + '1.' + extension2
            if extension1 == "png":
                im = im.convert("RGB")    # если RGBA  а не RGB
            im.save(Path_file[0] + '\\' + str2)
            count += 1
            S = []
    if count == 0:    # нет файлов с нужным расширением
        return (2, 0)
        
    return (3, count)        # конвертация прошла успешно
    
    
ext1 = "jpg"
ext2 = "png"
path1 = 'E:\PROG\IMAGES'
flag = True    # поиск файлов и внутри подкаталогов, False - только в текущем
success, count_f = convert(ext1, ext2)
if success == 0:
    print("Каталог не найден")
elif success == 1:
    print("Каталог пуст")
elif success == 2:
    print("В текущем каталоге нет", ext1, "- файлов")
elif success == 3:
    print("Формат", count_f, ext1, "- файлов изменен на", ext2)
    