# ПОПЫТКА УПОРЯДОЧИТЬ МАССИВ ПО ВОЗРАСТАНИЮ С ПОМОЩЬЮ ОДНОГО ИЗ 2-Х ПРИЕМОВ
def Football(F, N):

    # ф-я проверяет упорядочен ли массив по возрастанию
    def result(L):
        res = False
        for i in range(len(L) - 1):
            if L[i] < L[i + 1]:
                res = True
            else:
                res = False
                break
        return res

    # правило 1 - перестановка 2-х чисел
    def rule1(F):
        for i in range(len(F) - 1):
            if F[i] < F[i + 1]:    # проверяем рядом стоящие значения на возрастание
                continue
            else:
                k1 = i
                L1 = F[:]
                L1[k1], L1[k1 +1] = L1[k1 + 1], L1[k1]    # если следующий меньше предыдущего то меняем их местами и проверяем весь массив
                if result(L1):
                    return True
                else:
                    L1 = F[:]
                    if min(L1[k1:]) < L1[k1]:    # если предыдущая проверка не прошла, ищем минимальное в срезе
                        k2 = L1.index(min(L1[k1:]))
                        L1[k1], L1[k2] = L1[k2], L1[k1]
                        if result(L1):
                            return True
                        else:
                            return False
                    else:
                        return False
        return False

    
    # правило 2 - меняем на обратный порядок кусок последовательности в массиве
    def rule2(F):
        for i in range(len(F) - 1):
            if F[i] < F[i + 1]:    # проверяем рядом стоящие значения на возрастание
                continue
            else:
                k1 = i
                for j in range(k1, len(F) - 1):
                    if  F[j] > F[j + 1]:
                        k2 = j + 1
                        continue
                    else:
                        break
                L1 = F[:k1]
                L2 = F[k1:k2 + 1]
                L3 = F[k2 + 1:]
                L2.sort()
                if L1 == []:
                    L1 = L2 + L3
                else:
                    L1 = L1 + L2 + L3
                if result(L1):
                    return True
                else:
                    return False
        return False


    if rule1(F):
        return True
    else:
        if rule2(F):
            return True
        return False