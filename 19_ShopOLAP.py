# СВОДКА ПО ПРОДАЖАМ И СОРТИРОВКА ТОВАРОВ
def ShopOLAP(N, items):
    # создаем рабочий двумерный массив пар название-количество
    S = []
    si =[]
    for i in range(N):
        str1 = items1[i]
        si = str1.split()
        S.append(si)

    # сортируем массив по названиям товаров
    S.sort(key=lambda x: x[0])

    # считаем повторяющиеся товары и удаляем лишние записи
    k = 0
    while (k < len(S) - 1):    
        if S[k][0] == S[k + 1][0]:
            buffer = int(S[k][1]) + int(S[k + 1][1])
            S[k][1] = str(buffer)
            S.pop(k + 1)
        else:
            k = k + 1

    # сортируем массив по количеству проданных товаров
    S.sort(key=lambda x: x[1], reverse = True)

    # переводим двумерный массив в одномерный строковый
    S1 = []
    for i in range(len(S)):
        S1.append(S[i][0] + " " + S[i][1])
    return S1