# ПРОВЕРКА ВАЛИДНОСТИ ПАРОЛЕЙ
def SherlockValidString(s):
    
    S = []
    si = []
    si.append(s[0])
    i = 1
    si.append(i)
    S.append(si)
    si =[]
    while(i < len(s)):
        flag = False
        for j in range(len(S)):
            if s[i] == S[j][0]:
                S[j][1] += 1
                flag = True
                break
        if flag:
            i += 1
            continue
        si.append(s[i])
        si.append(1)
        S.append(si)
        si = []            
        i += 1

    # формируем массив - количества вхождений букв
    L = []
    for i in range(len(S)):
        L.append(S[i][1])

    # проверяем равно ли количество вхождений для каждой из букв
    for i in range(len(L)):
        if L[i] == L[0]:
            flag = True
        else:
            flag = False
            break
    if flag:
        return flag
    # если убрать одну букву - станет ли количество вхождений равным
    for i in range(len(L)):
        L1 = []
        for j in range(len(L)):
            L1.append(L[j])
        L1[i] = L1[i] - 1
        if L1[i] == 0:
            L1.pop(i)
        for j in range(len(L1)):
            if L1[j] == L1[0]:
                flag = True
            else:
                flag = False
                break
        if flag:
            return flag
    return flag