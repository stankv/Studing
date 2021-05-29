# РЕКУРСИВНАЯ ФУНКЦИЯ
# Расчёт длины списка, для которого разрешена только одна операция удаления первого элемента pop(0)
def LengthOfList(L):
    if L == []:
        return 0
    else:
        L.pop(0)
        return (1 + LengthOfList(L))

S = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(LengthOfList(S))