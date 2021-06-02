# ИСПОЛЬЗОВАНИЕ РЕКУРСИВНОЙ ФУНКЦИИ
# Поиск всех файлов в заданном каталоге, включая файлы, расположенные в подкаталогах произвольной вложенности

import os

def FindFiles(path):

    def Solving(pathtodir):
        for root, dirs, files in os.walk(pathtodir):
            for file in files:
                filelist.append(os.path.join(root,file))
        return filelist

    filelist = []
    if not os.path.isdir(path):    #  проверка существования каталога
        return filelist
    else:
        filelist = Solving(path)
        return filelist
        

my_path ="E:\PROG"
filelist1 = FindFiles(my_path)
if filelist1 == []:
    print("Каталог не найден")
else:
    for name in filelist1:
        print(name)