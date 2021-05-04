# ВРАЩЕНИЕ МАТРИЦЫ (В ЛЮБУЮ СТОРОНУ)
def MatrixTurn(Matrix, M, N, T):

    # вращает вправо при Т>0, и влево при Т<0
    def shift(lst, steps):
        if steps < 0:
            steps = abs(steps)
            for i in range(steps):
                lst.append(lst.pop(0))
        else:
            for i in range(steps):
                lst.insert(0, lst.pop())

    # получение массивов - внутренних "окружностей". Параметры массива глобальные
    def reading(k):
        m1 = 0 + k
        m2 = M - 1 - k
        n1 = 0 + k
        n2 = N - 1 - k
        for j in range(n1,n2):
            L.append(S[m1][j])
        for i in range(m1,m2):
            L.append(S[i][n2])
        for j in range(n2,n1,-1):
            L.append(S[m2][j])
        for i in range(m2,m1,-1):
            L.append(S[i][n1])
        return L
    
    # запись окружности в массив. Параметры массива глобальные
    def writing(k):
        m1 = 0 + k
        m2 = M - 1 - k
        n1 = 0 + k
        n2 = N - 1 - k
        l = 0
        while(l < len(L)):
            for j in range(n1,n2):
                S[m1][j] = L[l]
                l += 1
            for i in range(m1,m2):
                S[i][n2] = L[l]
                l += 1
            for j in range(n2,n1,-1):
                S[m2][j] = L[l]
                l += 1
            for i in range(m2,m1,-1):
                S[i][n1] =L[l]
                l += 1
        return S

    # перевод из массива строк в матрицу символов
    S = []
    for i in range(M):
        b = []
        for j in range(N):
            b.append(Matrix[i][j])
        S.append(b)
    
    for k in range(int(min(M / 2, N / 2))): # от внешнего ко внутреннему, по кругам
        L = []
        L = reading(k)  # читаем
        shift(L, T)     # сдвигаем
        S = writing(k)  # пишем обратно

    # запись в текстовом формате
    for i in range(M):
        Matrix[i] = "".join(S[i])