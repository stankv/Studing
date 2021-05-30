# РЕКУРСИВНАЯ ФУНКЦИЯ
# Печать только чётных значений из списка
def PrintEvenValues(L):
    if not L:
        print()
        return 0
    else:
        digit = L.pop(0)
        if (digit % 2) == 0:
            print(" ", digit, end='')
        return PrintEvenValues(L) 

S = [2,5,7,6,7,9,8,10,11,18,27,14,32,3]
PrintEvenValues(S)