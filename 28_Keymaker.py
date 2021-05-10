def Keymaker(k):
    S = []
    stroka = ""
    # создаем массив закрытых дверей
    for i in range(k):
        S.append("0")

    stroka = "".join(S)
    #print(stroka)
    
    n = 0
    for i in range(k):
        for j in range(n, k, n + 1):
            if S[j] == "0":
                S[j] = "1"
            else:
                S[j] = "0"
        #print(n + 1, " ", end = '')
        stroka = "".join(S)
        #print(stroka)
        n += 1
    return stroka