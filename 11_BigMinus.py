def BigMinus(s1, s2):
    # если оба числа оказались изначально одинаковы, то возвращаем 0
    if s1 == s2:
        return "0"
    
    # для цикла сначала выбираем меньшее число
    if len(s1) < len(s2):
        N = len(s1)
        str1 = s2    # определяем: str1 - уменьшаемое
        str2 = s1    # str2 - вычитаемое
    elif len(s1) > len(s2):
        N = len(s2)
        str1 = s1
        str2 = s2
    # при равной длине одно число может быть больше другого
    elif len(s1) == len(s2):
        N = len(s1)
        for i in range(N):
            if s1[i] == s2[i]:
                continue
            elif s1[i] > s2[i]:
                str1 = s1
                str2 = s2
                break
            elif s1[i] < s2[i]:
                str1 = s2
                str2 = s1
                break
        
    # для удобства и упрощения переворачиваем строки
    str1 = str1[::-1]
    str2 = str2[::-1]

    # вычитаем из большего (str1) меньшее (str2)
    Str1 = list(str1)
    Str2 = list(str2)
    for i in range(N):
        if Str1[i] == Str2[i]:
            Str1[i] = "0"
        elif int(Str1[i]) > int(Str2[i]):
            Str1[i] = str(int(Str1[i]) - int(Str2[i]))
        elif int(Str1[i]) < int(Str2[i]):
            k = int(Str1[i]) + 10 - int(Str2[i])
            Str1[i] = str(k)
            Str1[i + 1] = str(int(Str1[i + 1] - 1))
    
    # переворачиваем получившийся массив Str1 обратно
    Str1 = list(reversed(Str1))
    # в начале могут оказатся подряд несколько нулей, удаляем их
    for i in range(N):
        if Str1[i] == "0":
            Str1[i] = ""
        else:
            break
    str1 = "".join(Str1)

    return str1