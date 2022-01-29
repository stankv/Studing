# ДЕРЕВЬЯ.
# Построение сбалансированного бинарного дерева поиска в массиве.

def GenerateBBSTArray(a):

    def BBST_len(input_list):    # вычисление длины массива для дерева
        b = sorted(input_list)
        Tree_Depth = 0    # считаем, что глубина корня есть ноль
        while len(b) > 0:
            center = len(b) // 2
            b = b[:center]
            Tree_Depth += 1
        Tree_Depth -= 1
        return 2 ** (Tree_Depth + 1) - 1


    def AddKey(a, BBSTArray, I=0):
        index_center = len(a) // 2
        if a != []:
            BBSTArray[I] = a[index_center]
            AddKey(a[:index_center], BBSTArray, 2*I+1)
            AddKey(a[index_center + 1:], BBSTArray, 2*I+2)
        return BBSTArray

    if len(a) == 1:
        return a
    elif a is None or a == []:
        return None
    a.sort()
    BBSTArray = [None] * BBST_len(a)
    return AddKey(a, BBSTArray)

#z = []
#z = [1]
#z = [1,2,3,4]
#z = [7,2,3,1,4,8,9,6,10,5,0]
#z = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#print(GenerateBBSTArray(z))