def TheRabbitsFoot(s, encode):
    def Coder(s):
        # удаляем из строки все пробелы
        s1 = ""
        for ani in s:
            if ani != " ":
                s1 = s1 + ani
        # вычисляем размер матрицы
        N = len(s1)
        n = pow(N, 0.5)
        row = int(n)
        column = int(n * 10) - row * 10
        if column == 0:
            column = row
        if (row * column) < N:
            while((row * column) < N):
                row += 1
        N = row * column    # размер рабочей матрицы
        # дополняем строку пробелами чтобы влезала полностью в массив
        if len(s1) < N:
            for i in range(N - len(s1)):
                s1 = s1 + " "
        # формируем матрицу
        Matrix = []
        count = 0
        for i in range(row):
            b = []
            for j in range(column):
                b.append(s1[count])
                count += 1
            Matrix.append(b)
        # шифруем данные
        s1 = ""
        for i in range(column):
            for j in range(row):
                if Matrix[j][i] == " ":
                    s1 += ""
                else:
                    s1 += Matrix[j][i]
            if i < (column - 1):
                s1 += " "
        return s1

    def Decoder(s):
        # декодируем строку s
        S = s.split()    # разбиваем строку на слова
        # удаляем из строки все пробелы
        s1 = ""
        for ani in s:
            if ani != " ":
                s1 = s1 + ani
        N = len(S[0])    # "длина" цикла по буквам слова
        s2 = ""
        i = 0
        k = 0
        L = len(s1)
        while(i < N):
            for ani in S:
                s2 = s2 + ani[i]
                k = k + 1
                if k == L:
                    break
            i = i + 1
        return s2

    if encode == True:
        result = Coder(s)
    elif encode == False:
        result = Decoder(s)
    return result