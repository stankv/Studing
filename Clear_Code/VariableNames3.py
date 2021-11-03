# 7.1 Правильное именование булевых переменных
# 1. Рассматриваем код решения задачи "Машинное распознавание паттернов" курса "28 задач"
# Изменены имена переменных в строках: 25 (32, 35)
def LineAnalysis(line):
    # строка должна начинаться и заканчиваться "*"
    if line[0] != "*" or line[len(line) - 1] != "*":
        return False

    # проверяем отдельные исключительные случаи
    if line == "*" or line == "**" or line == "***":
        return True

    # определяем единый шаблон в строке
    template = ""
    for i in range(len(line)):
        template += line[i]
        if (line[i] != "*" and line[i + 1] == "*") or ((line[i] == "*" and line[i + 1] == "*")):
            k = i + 1
            break
    if len(line) > 1:
        template += line[i + 1]

    # идем по строке и проверяем соответствие шаблону
    substr = ""
    is_correct = True    # было flag
    if k <= (len(line) - 1):
        for i in range(k, len(line) - 1):
            substr += line[i]
            if line[i] != "*" and line[i + 1] == "*":
                substr += line[i + 1]
                if substr != template:
                    is_correct = False
                    break
                substr = ""
    return is_correct

# 2. Рассматриваем код решения задачи "Безумный Макс" курса "28 задач"
# Изменены имена переменных в строках: 40 (41, 42, 50, 56, 57, 58, 62)
def MadMax(N, Tele):
    is_not_sorted = True    # было xchange
    while(is_not_sorted):
        is_not_sorted = False # предполагаем, что массив уже отсортирован
        for i in range(N - 1):
            if Tele[i] > Tele[i+1]:
            # нашли элементы,
            # неупорядоченные по возрастанию:
            # меняем их местами:
                Tele[i], Tele[i+1] = Tele[i+1], Tele[i]
            # цикл проверки массива надо продожить снова:
                is_not_sorted = True
                
    # меняем местами срединный элемент и последний (наибольший)
    Tele[N // 2 ], Tele[N - 1] = Tele[N - 1], Tele[N // 2]
   
    # с середины сортируем элементы по убыванию   
    is_not_sorted = True
    while(is_not_sorted):
        is_not_sorted = False
        for i in range((N // 2) + 1, N - 1):
            if Tele[i] < Tele[i+1]:
                Tele[i + 1], Tele[i] = Tele[i], Tele[i + 1]
                is_not_sorted = True
    return Tele

# 3. Рассматриваем код решения задачи "Восстановление таблицы зарплат" курса "28 задач"
# Изменены имена переменных в строках: 79 (80, 81, 85, 87, 88, 89, 93)
def SynchronizingTables(N, ids, salary):
    
    #ids_new = ids    # делаем копию массива для дальнейшей работы
    ids_new = []
    for i in range(N):
        ids_new.append(ids[i])
    
    salary_new = []
    for i in range(N):
        salary_new.append(salary[i])
    
    # сортируем оба списка по возрастанию
    is_not_sorted = True    # было xchange
    while(is_not_sorted):
        is_not_sorted = False # предполагаем, что массив уже отсортирован
        for i in range(N - 1):
            if ids_new[i] > ids_new[i+1]:
                ids_new[i], ids_new[i+1] = ids_new[i+1], ids_new[i]
                is_not_sorted = True

    is_not_sorted = True 
    while(is_not_sorted):
        is_not_sorted = False
        for i in range(N - 1):
            if salary_new[i] > salary_new[i+1]:
                salary_new[i], salary_new[i+1] = salary_new[i+1], salary_new[i]
                is_not_sorted = True
 
    for i in range(N):
        k = ids[i]    # читаем номер сотрудника
        # ищем в отсортированном массиве этот номер и получаем номер элемента
        for j in range(N):
            if ids_new[j] == k:
                salary[i] = salary_new[j]
                break
    return salary

# 4. Рассматриваем код решения задачи "Танковый раш" курса "28 задач"
# Изменены имена переменных в строках: 129 (139, 142, 145, 146, 147, 151)
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
    success = False    # было flag
    for i in range(H1):
        for j in range(W1):
            if Matrix1[i][j] == Matrix2[0][0]:    # если найден первый символ, то проверяем может ли вмещаться в этом месте подматрица в матрицу
                if (i + H2) <= H1 and (j + W2) <= W1:
                    # проверка вхождения подматрицы
                    k = 0
                    for i1 in range(H2):
                        for j1 in range(W2):
                            if Matrix1[i + i1][j + j1] == Matrix2[i1][j1]:
                                success = True
                                k += 1    # счетчик совпадений элементов матриц
                            else:
                                success = False
                                break
                            if k == (H2 * W2):
                                return success
                        if not success:
                            success = False
                            break
                else:
                    continue
    return success

# 5. Рассматриваем код решения задачи "Мистер Робот и Корпорация Зла" курса "28 задач"
# Изменены имена переменных в строках: 159 (160, 163, 175, 176, 178, 181, 183)

# СОРТИРОВКА МАССИВА ПО ВОЗРАСТАНИЮ ПУТЕМ ЦИКЛИЧЕСКИХ ПЕРЕСТАНОВОК 3-Х БЛИЖАЙШИХ ЧИСЕЛ
# Возвращает True если массив отсортирован, и False если невозможно отсортировать.
def MisterRobot(N, data):
    is_sorted = False    # - элементы массива не отсортированы по возрастанию
    while(not is_sorted):
        for i in range(N - 2):
            if data[i] < data[i + 1] and data[i + 1] < data[i + 2]:
                is_sorted = True
                continue
            else:
                a0 = data[i]
                a1 = data[i + 1]
                a2 = data[i + 2]
                while(data[i] > data[i + 1] or data[i + 1] > data[i + 2]):
                    buffer = data[i]
                    data[i] = data[i + 1]
                    data[i + 1] = data[i + 2]
                    data[i + 2] = buffer
                    if (data[i] == a0 and data[i + 1] == a1 and data[i + 2] == a2):
                        is_sorted = False
                        return is_sorted
        # проверяем есть ли неотсортированные элементы в массиве
        is_sorted = True
        for j in range(N - 1):
            if data[j + 1] < data[j]:
                is_sorted = False
                break
    return is_sorted

# 7.2 Типичные имена булевых переменных
# 1. Рассматриваем код решения задачи "Танковый раш" курса "28 задач" (см. выше)
# Изменены имена переменных в строках: 129 (139, 142, 145, 146, 147, 151): flag -> success

# 2. Рассматриваем код решения задачи "Шерлок Холмс и механическая шкатулка" курса "28 задач"
# Изменены имена переменных в строках: 203 (207, 209): flag -> done
# Изменены имена переменных в строках: 229 (231, 233, 246, 248, 250): flag -> found
# Введена переменная success (226, 236). Изменены имена переменных в строках: 234 (252, 253): flag -> success

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
        done = False    # было flag
        for j in range(len(S)):
            if s[i] == S[j][0]:
                S[j][1] += 1
                done = True
                break
        if done:
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
    success = True
    for i in range(len(L)):
        if L[i] == L[0]:
            found = True    # было flag
        else:
            found = False
            break
    if found:
        return success
    # если убрать одну букву - станет ли количество вхождений равным
    success = False
    for i in range(len(L)):
        L1 = []
        for j in range(len(L)):
            L1.append(L[j])
        L1[i] = L1[i] - 1
        if L1[i] == 0:
            L1.pop(i)
        for j in range(len(L1)):
            if L1[j] == L1[0]:
                found = True
            else:
                found = False
                break
        if found:
            success = True
            return success
    return success

# 7.3 Cлучай, когда вместо индексов циклов i, j, k нагляднее использовать более выразительное имя
# Рассматриваем код решения задачи "Освобождение Государства Квадратов" курса "28 задач"
# Изменены имена индексов в строках: 260 (285): i -> x
# Изменены имена индексов в строках: 263 (286): j -> y
# (поскольку индексы циклов по-сути есть координаты x и y).
def ConquestCampaign(N, M, L, battalion):
    S = []
    for x in range(N):    # было i
        b = []
        for y in range(M):    # было j
            b.append(0)
        S.append(b)
        
    count = 0
    L2 = 0
    for i in range(L * 2):
        if i % 2 == 0:
            x = battalion[i] - 1
        else:
            y = battalion[i] - 1
        count = count + 1
        if count % 2 == 0:
            if x >= 0 and x < N and y >=0 and y < M and S[x][y] == 0:
                S[x][y] = 1
                L2 = L2 + 1
    if L2 == 0:
        return 0    
    
    Day = 1
    cell = N * M - L2
    while cell > 0:
        for x in range(N):
            for y in range(M):
                if S[x][y] == Day:
                    if (x + 1) < N and S[x + 1][y] == 0:
                        S[x + 1][y] = Day + 1
                    if (x - 1) >= 0 and S[x - 1][y] == 0:
                        S[x - 1][y] = Day + 1
                    if (y + 1) < M and S[x][y + 1] == 0:
                        S[x][y + 1] = Day + 1
                    if (y - 1) >= 0 and S[x][y - 1] == 0:
                        S[x][y - 1] = Day + 1

        for x in range(N):
            for y in range(M):
                if S[x][y] > Day:
                    cell -= 1
        Day += 1
        if Day > N * M:
            Day = N * M + 1
            break
    return Day

# 7.4 Использование пары имен - антонимов.
# Рассматриваем код решения задачи "Оптимизация беспилотного трафика" курса "28 задач"
# Изменены имена переменных: Distance1 -> prev, Distance2 -> next
def Unmanned(L, N, track):
    T = 0     # пройденный путь (время)
    prev = 0
    # случай когда светофоры дальше чем финишная точка
    if track[0][0] >= L:
        return L
    # движемся по отрезкам пути (от сфетофора к светофору)
    # считываем данные о ближайшем светофоре
    for i in range(N):
        next = track[i][0]
        red = track[i][1]
        green = track[i][2]
        # едем или стоим на светофоре ( и сколько стоим)
        Distance = next - prev
        T = T + Distance
        stop = T % (red + green)
        if stop >= red:    # красный перестал гореть
            stop = 0
        else:
            stop = red - stop    # красный горит и будет еще гореть столько моментов времени
        T = T + stop
        prev = next
    # все светофоры проехали, остался прямой участок пути до финиша
    T = T + (L - prev)
    return T

# 7.5 Случай, когда временные переменные надо переименовать, и от которых, возможно, можно полностью избавиться. 
# Рассматриваем код решения задачи "Разблокировка мобильных телефонов" курса "28 задач"
# Изменены имена переменных: res -> celoe, ost -> ostatok (строки 357, 358)
def PatternUnlock(N, hits):
    subS = ["62", "26", "27", "72", "29", "92", "24", "42", "15", "51", "53", "35", "18", "81", "38", "83"]
    hits1 = []
    # преобразуем входной массив чисел в строку
    for i in range(N):
        hits1.append(str(hits[i]))
    hits1 = "".join(hits1)
    
    # поиск подстрок в строке
    count = 0
    for ani in subS:
        k = hits1.find(ani)
        if k >= 0:
            count += 1
    # считаем длину линии
    res = N - 1 - count + count * 1.414213562373095
    # округляем до 5-го знака
    celoe = int(res * 1E6)    # было res
    ostatok = celoe % 10      # было ost
    celoe = celoe // 10
    if ostatok >= 5:
        celoe = celoe + 1
    res = str(celoe)
    # удаляем нули если они есть
    result = []
    for ani in res:
        if ani == "0":
            continue
        result.append(ani)
    result = "".join(result)
    return result

# От временных переменных celoe и ostatok можно полностью избавиться, переписав участок кода (строки 355 - 362) так:
    res = int((N - 1 - count + count * 1.414213562373095) * 1E6)
    if res % 10 >= 5:
        res = (res // 10) + 1
    else:
        res = res // 10
    res = str(res)