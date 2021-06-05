# ИСПОЛЬЗОВАНИЕ РЕКУРСИВНОЙ ФУНКЦИИ
# Поиск всех файлов в заданном каталоге, включая файлы, расположенные в подкаталогах произвольной вложенности

import os

def Solve(path1):
    A = []
    for root, dirs, files in os.walk(path1):
        # Текущий каталог в рут. перебираем файлы из списка files 
        for file in files:
            A.append(os.path.join(root,file))
        for dir in dirs:
            Solve(os.path.join(root,dir))
    return A

def FindFiles(path):
    A = []
    if not os.path.isdir(path):    #  проверка существования каталога
        A.append(1)
        return A
    else:
        return Solve(path)


my_path ="E:\PROG\Temp1"
filelist1 = FindFiles(my_path)
if filelist1 == []:
    print("Каталог пустой")
elif filelist1 == [1]:
    print("Каталог не найден")
else:
    for name in filelist1:
        print(name)