# Переменные и их значения
# 1 - 4. Рассматриваем код решения задачи "Поездка на мотоцикле" курса "28 задач"
# 1. В соответствии с условиями задачи ф-я odometer(N) получает параметром массив N целых чисел (N >= 2) 
# с индексацией с нуля. Введена проверка размера массива (д.б. >=2), строки 10,11,12.
# 2. Переменные, используемые в вычислениях внутри цикла time_current, time_elapsed, distance_travelled, 
# count, объявлены и инициированы непосредственно перед циклом - строки 13, 14, 15, 16
# 3. Введена проверка значений N[] на целочисленность (тип int), строки 18, 19, 20.
# 4. После завершения вычислений переменным присвоены "недопустимые" значения, строки 29,30,31,32.
def odometer(N):
    if len(N) < 2:
        print("array dimension less than 2")
        return
    time_current = 0        # время движения на конкретном (текущем) участке пути
    time_elapsed = 0        # полное время движения до текущего участка пути
    distance_travelled = 0  # общее пройденное расстояние
    count = 0
    for i in range(len(N)):
        if type(N[i]) is not int:
            print("invalid array element value", N[i])
            return
        if i % 2 == 0:
            velocity_current = N[i]
        else:
            time_current = N[i] - time_elapsed
            time_elapsed = N[i]
        count = count + 1
        if count % 2 == 0 and count != 0:
            distance_travelled += velocity_current * time_current
    time_current = -1
    time_elapsed = -1
    count = -1
    N = None
    return distance_travelled

# 5 - 15. Рассматриваем код решения задачи "Освобождение Государства Квадратов" курса "28 задач"
# В соответствии с условиями задачи аргументы N,M,L >=1 и целочисленны, и L*2 == len(battalion), а значения массива
# battalion[] есть int, причем >=1.
# 5. Введена проверка корректности входящих данных N,M,L: строки 57-63
# 6. Введена проверка корректности входных данных L*2 == len(battalion): строки 66-68
# 7. Непосредственно перед использованием в циклах, объявлены и инициированы переменные-массивы 
# State_of_squares[] и Squares_column[]: строки 69 и 71.
# 8. Поскольку вспомогательный массив Squares_column[] после завершения цикла нигде далее не используется, ему
# присваивается "недопустимое" значение None: строка 75
# 9. Непосредственно перед использованием в циклах, объявлены и инициированы целочисленные положительные переменные: 
# аккумулятор count и squares_captured: строки 77, 78
# 10. Поскольку count после цикла нигде не используется, то ему присваивается "недопустимое" значение -1: строка 92
# 11. Введена проверка корректности входящих данных - целочисленность значений массива battalion 
# и что они >=1 : строки 80-82
# 12. Поскольку после цикла переменная-массив battalion более не используется, то присваиваем ей "недопустимое" 
# значение None: строка 93
# 13. Непосредственно перед использованием в циклах, объявлены и инициированы целочисленные положительные переменные:
# Day и squares_not_captured: строки 97 и 98.
# 14. Поскольку squares_not_captured после вычислений в циклах далее больше не используется, то присваиваем ей "недопустимое" 
# значение -1: строка 120
# 15. Аналогично для переменной squares_captured: строка 119. Также можно сделать для переменных N,M,L.
def ConquestCampaign(N, M, L, battalion):
    if type(N) is not int or N < 1:
        print("invalid value N = ", N)
        return
    elif type(M) is not int or M < 1:
        print("invalid value M = ", M)
        return
    elif type(L) is not int or L < 1:
        print("invalid value L = ", L)
        return
    if L*2 != len(battalion):
        print("invalid array dimension battalion = ", len(battalion), "for L = ", L)
        return
    State_of_squares = []    # массив квадратов "государства квадратов"
    for x in range(N):
        Squares_column = []
        for y in range(M):
            Squares_column.append(0)
        State_of_squares.append(Squares_column)
    Squares_column = None    # либо Squares_column = []
        
    count = 0
    squares_captured = 0    # количество захваченных квадратов
    for i in range(L * 2):
        if type(battalion[i]) is not int or battalion[i] < 1:
            print("invalid battalion array element value", battalion[i])
            return
        if i % 2 == 0:
            x = battalion[i] - 1
        else:
            y = battalion[i] - 1
        count = count + 1
        if count % 2 == 0:
            if x >= 0 and x < N and y >=0 and y < M and State_of_squares[x][y] == 0:
                State_of_squares[x][y] = 1    # помечаем квадраты, где высадился десант 
                squares_captured = squares_captured + 1
    count = -1
    battalion = None
    if squares_captured == 0:    # десант высадился вне государства квадратов
        return 0    
    
    Day = 1
    squares_not_captured = N * M - squares_captured    # количество не захваченных квадратов
    while squares_not_captured > 0:
        for x in range(N):
            for y in range(M):
                if State_of_squares[x][y] == Day:
                    if (x + 1) < N and State_of_squares[x + 1][y] == 0:
                        State_of_squares[x + 1][y] = Day + 1
                    if (x - 1) >= 0 and State_of_squares[x - 1][y] == 0:
                        State_of_squares[x - 1][y] = Day + 1
                    if (y + 1) < M and State_of_squares[x][y + 1] == 0:
                        State_of_squares[x][y + 1] = Day + 1
                    if (y - 1) >= 0 and State_of_squares[x][y - 1] == 0:
                        State_of_squares[x][y - 1] = Day + 1
        for x in range(N):
            for y in range(M):
                if State_of_squares[x][y] > Day:
                    squares_not_captured -= 1
        Day += 1
        if Day > N * M:
            Day = N * M + 1
            break
    squares_captured = -1
    squares_not_captured = -1
    return Day

# Также для проверок корректности входных данных или значений переменных в процессе вычислений, можно 
# использовать конструкцию try - except, assert или генерировать исключения с помощью raise.