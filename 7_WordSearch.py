def WordSearch(lenght, s, subs):
    # поиск пробелов в строке и их позиций
    P = []
    S1 = []
    P.append(0)
    for i in range(len(s)):
        if s[i] == " ":
            P.append(i)

    # формируем массив строк заданной ширины из длинной строки
    P.append(len(s) - 1)
    k = 1
    i1 = P[0]
    i2 = P[1] 
    if(i2 == 0): 
        i1 = 1  
    Np = len(P)
    Ns = len(s)

    n1 = 0
    n2 = 0

    while (k < Np and n1 < Ns + 1):
        n1 = n1 + 1
        if i2 - i1 <= lenght:
            i3 = i2
            while(i3 - i1 <= lenght and n2 < Ns + 1):
                n2 = n2 + 1
                k = k + 1
                if k >= Np:
                    #i3 = P[Np-1]
                    break
                i3 = P[k]
            k = k - 1
            i2 = P[k]
            i3 = i2
            if k == Np - 1:
                i3 = Ns
            if i3 - i1 + 1 >0:
                S1.append(s[i1:i3])
            i1 = i2 + 1
            k = k + 1
            if k >= Np:
                break
            i2 = P[k]
            if k == Np-1:
               i2 = i2 + 1
        else:
            S1.append(s[i1:i1 + lenght])
            i1 = i1 + lenght 
 
    # ищем нужную подстроку в строках массива и формируем выходной массив
    S2 = []
    for i in range(len(S1)):
        if S1[i].find(subs + ' ') == 0 or S1[i].find(' ' + subs + ' ') > 0 or S1[i].endswith(' ' + subs) or S1[i] == subs:
            S2.append(1)
        else: 
            S2.append(0)

    return S2