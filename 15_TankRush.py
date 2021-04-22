# ПОИСК МАТРИЦЫ В МАТРИЦЕ
def TankRush(H1, W1, S1, H2, W2, S2):
    # если размер подматрицы больше размера исходной матрицы то False
    if (H2 * W2) > (H1 * W1):
        return False
    # удаляем пробелы из входных строк
    S0 = S1.split()
    # создаем матрицы из входных данных
    Matrix1 = []
    Matrix2 = []
    for ani in S0:
        b = []
        for j in range(W1):
            b.append(ani[j])
        Matrix1.append(b)
    S0 = S2.split()
    for ani in S0:
        b = []
        for j in range(W2):
            b.append(ani[j])
        Matrix2.append(b)
    
    # поиск подматрицы в исходной матрице
    flag = False
    for i in range(H1):
        for j in range(W1):
            if Matrix1[i][j] == Matrix2[0][0]:    # если найден первый символ, то проверяем может ли вмещаться в этом месте подматрица в матрицу
                if (i + H2) <= H1 and (j + W2) <= W1:
                    # проверка вхождения подматрицы
                    k = 0
                    for i1 in range(H2):
                        for j1 in range(W2):
                            if Matrix1[i + i1][j + j1] == Matrix2[i1][j1]:
                                flag = True
                                k += 1    # счетчик совпадений элементов матриц
                            else:
                                flag = False
                                break
                            if k == (H2 * W2):
                                return flag
                        if not flag:
                            flag = False
                            break
                else:
                    continue
    return flag