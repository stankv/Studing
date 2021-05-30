# РЕКУРСИВНАЯ ФУНКЦИЯ
# Печать элементов списка с чётными индексами
i = 0
def Calculation(L, i):
    if i == len(L) - 1:
        print()
        return 0
    else:
        if (i % 2) == 0:
            print(" ", L[i], end='')
        i += 1
        return Calculation(L, i)

def PrintItemsWithEvenIndexes(Spisok):
    starting_value_i = 0
    return Calculation(Spisok, starting_value_i)

S = [2,5,7,6,7,9,8,10,11,18,27,14,32,3]
PrintItemsWithEvenIndexes(S)