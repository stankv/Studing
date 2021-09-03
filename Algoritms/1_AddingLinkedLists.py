# ФУНКЦИЯ ПОЛУЧАЕТ НА ВХОД 2 СВЯЗАННЫХ СПИСКА, И ЕСЛИ ИХ ДЛИНЫ РАВНЫ ВОЗВРАЩАЕТ СПИСОК,
# КАЖДЫЙ ЭЛЕМЕНТ КОТОРОГО РАВЕН СУММЕ СООТВЕТСТВУЮЩИХ ЭЛЕМЕНТОВ СВЯЗАННЫХ СПИСКОВ.
def AddingLinkedLists(S1, S2):
    count1 = 0
    count2 = 0
    for node in S1:
        count1 += 1
    for node in S2:
        count2 += 1
    if count1 != count2:
        return None
    else:
        S = []
        for node in S1