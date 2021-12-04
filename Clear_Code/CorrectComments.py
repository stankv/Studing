# Правильные комментарии
# Внесите 12 правок в свои комментарии.

# 1 и 2. Рассматриваем код решения задачи "Поездка на мотоцикле" курса "28 задач"
# 1. Информативные комментарии (строки 8-10) раскрывают суть используемых переменных.
# 2. Строка 13: информативный комментарий раскрывает принцип "устройства" массива и работы с ним.
def odometer(N):
    time_current = 0        # время движения на конкретном (текущем) участке пути
    time_elapsed = 0        # полное время движения до текущего участка пути
    distance_travelled = 0  # общее пройденное расстояние
    count = 0
    for i in range(len(N)):
        if i % 2 == 0:    # эл-ты массива с четными индексами - скорость, с нечетными - пройденный путь
            velocity_current = N[i]
        else:
            time_current = N[i] - time_elapsed
            time_elapsed = N[i]
        count = count + 1
        if count % 2 == 0 and count != 0:
            distance_travelled += velocity_current * time_current
    return distance_travelled

# 3-5. Рассматриваем код решения задачи "Освобождение Государства Квадратов" курса "28 задач"
# 3. Информативные комментарии: строки 35, 44, 46, 50
# 4-5. Представление намерений: строки 33, 48
def ConquestCampaign(N, M, L, battalion):
    State_of_squares = []    # массив квадратов "государства квадратов"
    for x in range(N):
        Squares_column = []
        for y in range(M):
            Squares_column.append(0)
        State_of_squares.append(Squares_column)
    # Высадка десанта в квадраты с заданными координатами    
    count = 0
    squares_captured = 0    # количество захваченных квадратов
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
    # Захват десантом прилежаших квадратов (помечаем 1, а ранее захваченные помечаем 2, и т.д.)
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
    return Day

# 6. Рассматриваем код решения задачи "Разблокировка мобильных телефонов" курса "28 задач"
# Информативные комментарии: строки 79, 83, 89, 91, 98
def PatternUnlock(N, hits):
    Diagonal_elements = ["62", "26", "27", "72", "29", "92", "24", "42", "15", "51", "53", "35", "18", "81", "38", "83"]
    string_input = []
    # преобразуем входной массив чисел в строку
    for i in range(N):
        string_input.append(str(hits[i]))
    string_input = "".join(string_input)
    # поиск " диагональных" подстрок во входной строке
    number_of_diagonal_elements = 0
    for ani in Diagonal_elements:
        found = string_input.find(ani)
        if found >= 0:
            number_of_diagonal_elements += 1
    # считаем длину линии
    length_line = N - 1 - number_of_diagonal_elements + number_of_diagonal_elements * 1.414213562373095
    # округляем до 5-го знака
    celoe = int(length_line * 1E6)
    ostatok = celoe % 10
    celoe = celoe // 10
    if ostatok >= 5:
        celoe = celoe + 1
    length_line = str(celoe)
    # удаляем нули если они есть
    string_output = []
    for ani in length_line:
        if ani == "0":
            continue
        string_output.append(ani)
    string_output = "".join(string_output)
    return string_output

# 7. Рассматриваем код решения задачи "Экономим тонер" курса "28 задач"
# Прояснение: строка 120. Также можно ввести константу, например ANOTHER_SYMBOL = 23 и дать поясняющий комментарий.
def PrintingCosts(Line):
    TableSymbols = {" ": 0, "!": 9, "\"": 6, "#": 24, "$": 29, "%": 22, "&": 24, "\'": 3, "(": 12, ")": 12, "*": 17, "+": 13, 
                   ",": 7, "-": 7, ".": 4, "/": 10, "0": 22, "1": 19, "2": 22, "3": 23, "4": 21, "5": 27, "6": 26, "7": 16, 
                   "8": 23, "9": 26, ":": 8, ";": 11, "<": 10, "=": 14, ">": 10, "?": 15, "@": 32, "A": 24, "B": 29, "C": 20, 
                   "D": 26, "E": 26, "F": 20, "G": 25, "H": 25, "I": 18, "J": 18, "K": 21, "L": 16, "M": 28, "N": 25, "O": 26, 
                   "P": 23, "Q": 31, "R": 28, "S": 25, "T": 16, "U": 23, "V": 19, "W": 26, "X": 18, "Y": 14, "Z": 22, "[": 18, 
                   "\\": 10, "]": 18, "^": 7, "_": 8, "`": 3, "a": 23, "b": 25, "c": 17, "d": 25, "e": 23, "f": 18, "g": 30, 
                   "h": 21, "i": 15, "j": 20, "k": 21, "l": 16, "m": 22, "n": 18, "o": 20, "p": 25, "q": 25, "r": 13, "s": 21, 
                   "t": 17, "u": 17, "v": 13, "w": 19, "x": 13, "y": 24, "z": 19, "{": 18, "|": 12, "}": 18, "~": 9}
    result = 0
    for symbol in Line:
        result += TableSymbols.get(symbol, 23)    # если символа нет в таблице, то расход тонера = 23
    return result

# 8. Рассматриваем код решения задачи "Делаем национальный редактор "Лапоть"" курса "28 задач"
# Прояснение: строка 127 (и аналогично далее по коду) - раскрывает суть кода операции.
def BastShoe(command):
    # много кода ...
    if operation == "1":    # добавление строки к строке
        if index_S == -1:
            current_stroka = ""
        else:
            current_stroka = S[index_S]
        if flag:
            S = []
            S.append(current_stroka)
            current_stroka = current_stroka + stroka
            S.append(current_stroka)
            index_S = 1
            flag = False
        else:
            current_stroka = current_stroka + stroka
            S.append(current_stroka)
            index_S = index_S + 1
        return current_stroka
    # много кода.....

# 9. Рассматриваем код решения задачи "Восстановление таблицы зарплат" курса "28 задач"
# Предупреждения о последствиях: строки 150 и 155.
def SynchronizingTables(N, ids, salary):
    
    #ids_new = ids    # ссылка на тот же объект! изменение ids_new изменит и массив ids!
    ids_new = []    # делаем копию массива для дальнейшей работы
    for i in range(N):
        ids_new.append(ids[i])
    
    #salary_new = salary    # ссылка на тот же объект! изменение salary_new изменит и массив salary!
    salary_new = []
    for i in range(N):
        salary_new.append(salary[i])
    # много кода...

# 10 и 11. Рассматриваем код решения задачи "Ассоциативный массив" курса "Алгоритмы и структуры данных 1"
# 10. Усиление: строка 166.
# 11. Усиление: строка 171 - подчеркивает важность корректности входных данных.
class NativeDictionary:
    def __init__(self, sz):
        self.size = sz    # размер массива фиксирован и не должен быть превышен при применении!
        self.slots = [None] * self.size     # массив ключей
        self.values = [None] * self.size    # массив значений
        self.step = 3    # длина шага (количество слотов) для поиска следующего свободного слота

    # Метод по входному значению возвращает индекс слота
    def hash_fun(self, key):    # в качестве key поступают строки!
        sum = 0
        for i in key:
            sum += ord(i)
        return sum % self.size
    # много кода...

# 12. Рассматриваем код решения задачи "Двунаправленный связанный список" курса "Алгоритмы и структуры данных 1"
# https://github.com/stankv/Studing/blob/main/Algoritms/LinkedList2.py
# TODO: строка 207
class Node:
    def __init__(self, v):
        self.value = v      # значение узла
        self.prev = None    # указатель на предыдущий узел
        self.next = None    # указатель на следующий узел

# Задаем двунаправленный связанный список
class LinkedList2:  
    def __init__(self):     # Инициализация двусвязного списка
        self.head = None    # указатель на узел-голову списка
        self.tail = None    # указатель на завершающий узел
    
    # много кода...

    # 7. Метод вставки узла самым первым элементом
    def add_in_head(self, newNode):
        if self.head is None:    # если список пустой
            #self.head = newNode    # неверно, этого не достаточно
            self.add_in_tail(newNode)
            return
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        return

    # TODO: Метод используется только для отладки
    # 8. Отладочный вывод значений узлов всего списка
    #def print_all_nodes(self):
        #node = self.head
        #while node is not None:
            #print(node.value)
            #node = node.next