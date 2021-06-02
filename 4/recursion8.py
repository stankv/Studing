# ИСПОЛЬЗОВАНИЕ РЕКУРСИВНОЙ ФУНКЦИИ
# Поиск всех файлов в заданном каталоге, включая файлы, расположенные в подкаталогах произвольной вложенности

import os

def FindFiles(path):

    def Solving(pathtodir):
        for root, dirs, files in os.walk(pathtodir):
                for file in files:
                    filelist.append(os.path.join(root,file))
                if dirs == []:
                    return filelist
                else:
                    for dir in dirs:
                        return Solving(pathtodir + "\\" + dir)


    filelist = []
    if not os.path.isdir(path):    #  проверка существования каталога
        return filelist
    else:
        new_path = path
        Solving(path)
        for root, dirs, files in os.walk(path):
            k = 0
            for dirname in dirs:
                if k == 0:
                    k = 1
                    continue
                new_path = path + "\\" + dirname
                Solving(new_path)
            return filelist
        

my_path ="E:\PROG\Temp1"
filelist1 = FindFiles(my_path)
if filelist1 == []:
    print("Каталог не найден")
else:
    for name in filelist1:
        print(name)