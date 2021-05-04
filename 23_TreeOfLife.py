# МОДЕЛИРОВАНИЕ N ЛЕТ РАЗВИТИЯ ДЕРЕВА
def TreeOfLife(H, W, N, tree):
    # переводим символы матрицы в нули и единицы
    S = []
    for i in range(H):
        b = []
        for j in range(W):
            if tree[i][j] == ".":
                b.append(0)
            else:
                b.append(1)
        S.append(b)

    # вывод вида дерева
    #def view():
        #for i in range(H):
            #for j in range(W):
                #print(' ', S[i][j], end='')
            #print()
        #print()
        #print()
    #view()

    # моделируем рост дерева с годами
    k = 0
    while(k < N):
        k += 1
        flag = False
        for i in range(H):
            for j in range(W):
                S[i][j] += 1
                if S[i][j] >= 3:
                    flag = True
        # если есть ветки >= 3 лет
        if flag and (k % 2) == 0:
            for i in range(H):
                for j in range(W):
                    if S[i][j] > 2:
                        if i - 1 >= 0 and S[i - 1][j] < 3:
                            S[i - 1][j] = 0
                        if i + 1 < H and S[i + 1][j] < 3:
                            S[i + 1][j] = 0
                        if j - 1 >= 0 and S[i][j - 1] < 3:
                            S[i][j - 1] = 0
                        if j + 1 < W and S[i][j + 1] < 3:
                            S[i][j + 1] = 0
                        S[i][j] = 0
        #print(k)
        #view()

    # преобразуем к графическому виду для вывода
    tree = []
    for i in range(H):
        str1 = ""
        for j in range(W):
            if S[i][j] == 0:
                str2 = "."
            else:
                str2 = "+"
            str1 += str2
        tree.append(str1)

    return(tree)

#print(TreeOfLife(3, 4, 4, [".+..","..+.",".+.."]))