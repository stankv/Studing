# Имена, которые следует избегать. 12 примеров.

# 1. Рассматриваем код решения задачи "Поездка на мотоцикле" курса "28 задач"
# Изменены имена 3-х плохих переменных в строках: 7 (15, 19), 8 (15, 16) 
# и 9 (19, 20)
def odometer(N):
    time_current = 0        # было time: время движения на конкретном (текущем) участке пути
    time_elapsed = 0        # было time1: полное время движения до текущего участка пути
    distance_travelled = 0  # было S: общее пройденное расстояние
    count = 0
    for i in range(len(N)):
        if i % 2 == 0:
            velocity_current = N[i]    # было velocity
        else:
            time_current = N[i] - time_elapsed
            time_elapsed = N[i]
        count = count + 1
        if count % 2 == 0 and count != 0:
            distance_travelled += velocity_current * time_current
    return distance_travelled

# 2. Рассматриваем код решения задачи "Освобождение Государства Квадратов" курса "28 задач"
# Изменены имена 4-х плохих переменных в строках: 25, 27, 33, 48
def ConquestCampaign(N, M, L, battalion):
    State_of_squares = []    # было S: массив квадратов "государства квадратов"
    for x in range(N):
        Squares_column = []               # было b[]
        for y in range(M):
            Squares_column.append(0)
        State_of_squares.append(Squares_column)
        
    count = 0
    squares_captured = 0    # было L2: количество захваченных квадратов
    for i in range(L * 2):
        if i % 2 == 0:
            x = battalion[i] - 1
        else:
            y = battalion[i] - 1
        count = count + 1
        if count % 2 == 0:
            if x >= 0 and x < N and y >=0 and y < M and State_of_squares[x][y] == 0:
                State_of_squares[x][y] = 1    # помечаем квадраты, где высадился десант 
                squares_captured = squares_captured + 1
    if squares_captured == 0:    # десант высадился вне государства квадратов
        return 0    
    
    Day = 1
    squares_not_captured = N * M - squares_captured    # было cell: количество не захваченных квадратов
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
    return Day

# 3. Рассматриваем код решения задачи "Восстановление таблицы зарплат" курса "28 задач"
# Изменены имена 3-х плохих переменных в строках: 77, 81, 103
def SynchronizingTables(N, ids, salary):
    
    # делаем копии массивов для дальнейшей работы
    ids_copy = []    # было ids_new
    for i in range(N):
        ids_copy.append(ids[i])
    
    salary_copy = []    # было salary_new
    for i in range(N):
        salary_copy.append(salary[i])
    
    # сортируем оба списка по возрастанию
    is_not_sorted = True    # было xchange
    while(is_not_sorted):
        is_not_sorted = False # предполагаем, что массив уже отсортирован
        for i in range(N - 1):
            if ids_copy[i] > ids_copy[i+1]:
                ids_copy[i], ids_copy[i+1] = ids_copy[i+1], ids_copy[i]
                is_not_sorted = True

    is_not_sorted = True 
    while(is_not_sorted):
        is_not_sorted = False
        for i in range(N - 1):
            if salary_copy[i] > salary_copy[i+1]:
                salary_copy[i], salary_copy[i+1] = salary_copy[i+1], salary_copy[i]
                is_not_sorted = True
 
    for i in range(N):
        employee_id = ids[i]    # было k: читаем номер сотрудника
        # ищем в отсортированном массиве этот номер и получаем номер элемента
        for j in range(N):
            if ids_copy[j] == employee_id:
                salary[i] = salary_copy[j]
                break
    return salary

# 4. Рассматриваем код решения задачи "Разблокировка мобильных телефонов" курса "28 задач"
# Изменены имена 4-х плохих переменных в строках: 114, 116, 123, 125, 129, 138
def PatternUnlock(N, hits):
    Diagonal_elements = ["62", "26", "27", "72", "29", "92", "24", "42", "15", "51", "53", "35", "18", "81", "38", "83"]
           # было subS
    string_input = []    # было hits1
    # преобразуем входной массив чисел в строку
    for i in range(N):
        string_input.append(str(hits[i]))
    string_input = "".join(string_input)
    
    # поиск " диагональных" подстрок во входной строке
    number_of_diagonal_elements = 0    # было count
    for ani in Diagonal_elements:
        found = string_input.find(ani)    # было k
        if found >= 0:
            number_of_diagonal_elements += 1
    # считаем длину линии
    length_line = N - 1 - number_of_diagonal_elements + number_of_diagonal_elements * 1.414213562373095    # было res
    # округляем до 5-го знака
    celoe = int(length_line * 1E6)
    ostatok = celoe % 10
    celoe = celoe // 10
    if ostatok >= 5:
        celoe = celoe + 1
    length_line = str(celoe)
    # удаляем нули если они есть
    string_output = []    # было result[]
    for ani in length_line:
        if ani == "0":
            continue
        string_output.append(ani)
    string_output = "".join(string_output)
    return string_output