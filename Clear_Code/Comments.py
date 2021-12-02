# Комментарии
# Прокомментируйте 7 мест в своём коде там, где это явно уместно. 

# 1 и 2. Рассматриваем код решения задачи "Поездка на мотоцикле" курса "28 задач"
# 1. Уместные комментарии (строки 8-10) раскрывают суть используемых переменных.
# 2. Строка 13: комментарий раскрывает принцип "устройства" массива и работы с ним.
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

# 3-8. Рассматриваем код решения задачи "Разблокировка мобильных телефонов" курса "28 задач"
# Уместные комментарии (строки 26, 28, 34, 40, 42, 49) разбивают код на логические блоки, показывая какой блок что выполняет.
def PatternUnlock(N, hits):
    # массив "диагональных линий" (гипотенуз)
    subS = ["62", "26", "27", "72", "29", "92", "24", "42", "15", "51", "53", "35", "18", "81", "38", "83"]
    # преобразуем входной массив чисел hits[] в строку
    hits1 = []
    for i in range(N):
        hits1.append(str(hits[i]))
    hits1 = "".join(hits1)
    
    # поиск подстрок в строке (поиск "диагональных линий")
    count = 0
    for ani in subS:
        k = hits1.find(ani)
        if k >= 0:
            count += 1
    # считаем длину линии
    res = N - 1 - count + count * 1.414213562373095
    # округляем до 5-го знака
    res = int(res * 1E6)
    ost = res % 10
    res = res // 10
    if ost >= 5:
        res = res + 1
    res = str(res)
    # удаляем нули если они есть
    result = []
    for ani in res:
        if ani == "0":
            continue
        result.append(ani)
    result = "".join(result)
    return result

# 9-13. Рассматриваем код решения задачи "Реализация кэша (на основе хэш-таблицы)" курса "Алгоритмы и 
# структуры данных" - https://github.com/stankv/Studing/blob/main/Algoritms/NativeCache1.py
# Уместные комментарии в конструкторе класса NativeCache, расшифровывающие значения основных полей класса 
# (строки 64-68):
class NativeCache:
    def __init__(self, sz):
        self.size = sz                      # размер хэш-таблицы (желательно простое число)
        self.slots = [None] * self.size     # массив ключей
        self.values = [None] * self.size    # массив значений
        self.hits = [0] * self.size         # массив количества обращений к каждому ключу
        self.step = 3    # длина шага (количество слотов) для поиска следующего свободного слота

#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------

# Найдите 5 мест, где комментарии были излишни, удалите их и сделайте сам код более наглядным. 

# 1-3. Рассматриваем код решения задачи "Экономим тонер" курса "28 задач"
# Было:
def PrintingCosts(Line):
    # для обхода символов эскейп-последовательностей в строке, в интернете был найден этот код
    # ---------------------------------------------------------------------------------------
    escape_dict={'\a':r'\a',
                 '\b':r'\b',
                 '\c':r'\c',
                 '\f':r'\f',
                 '\n':r'\n',
                 '\r':r'\r',
                 '\t':r'\t',
                 '\v':r'\v',
                 '\'':r'\'',
                 '\"':r'\"'}

    def raw(text):
        """Returns a raw string representation of text"""
        new_string=''
        for char in text:
            try: 
                new_string += escape_dict[char]
            except KeyError: 
                new_string += char
        return new_string
    #-------------------------------------------------------------------------------------------
    # далее мой код решения самой задачи
    
    # таблица символов в виде списка
    TableSymbols = [" ", 0, "!", 9, "\"", 6, "#", 24, "$", 29, "%", 22, "&", 24, "\'", 3, "(", 12, ")", 12, "*", 17, "+", 13, 
                   ",", 7, "-", 7, ".", 4, "/", 10, "0", 22, "1", 19, "2", 22, "3", 23, "4", 21, "5", 27, "6", 26, "7", 16, 
                   "8", 23, "9", 26, ":", 8, ";", 11, "<", 10, "=", 14, ">", 10, "?", 15, "@", 32, "A", 24, "B", 29, "C", 20, 
                   "D", 26, "E", 26, "F", 20, "G", 25, "H", 25, "I", 18, "J", 18, "K", 21, "L", 16, "M", 28, "N", 25, "O", 26, 
                   "P", 23, "Q", 31, "R", 28, "S", 25, "T", 16, "U", 23, "V", 19, "W", 26, "X", 18, "Y", 14, "Z", 22, "[", 18, 
                   "\\", 10, "]", 18, "^", 7, "_", 8, "`", 3, "a", 23, "b", 25, "c", 17, "d", 25, "e", 23, "f", 18, "g", 30, 
                   "h", 21, "i", 15, "j", 20, "k", 21, "l", 16, "m", 22, "n", 18, "o", 20, "p", 25, "q", 25, "r", 13, "s", 21, 
                   "t", 17, "u", 17, "v", 13, "w", 19, "x", 13, "y", 24, "z", 19, "{", 18, "|", 12, "}", 18, "~", 9]
    
    res = 0
    N = len(TableSymbols)
    LineWork = raw(Line)
    switch = 0

    for ani in LineWork:
        for i in range(0, N, 2):
            if ani == TableSymbols[i]:
                res += TableSymbols[i + 1]
                switch = 1
                break
        if switch == 0:
            res += 23
        switch = 0
    return res
# Код решения задачи был переписан: 
# 1.массив TableSymbols[] (таблица символов) был заменен на словарь.
# 2. Код (строки 78-99) более не нужен и был удален
# 3. Код самого решения (строки 113-127) переписан более коротко и лаконично.
# При этом удалены ненужные комментарии (строки 78, 101, 103)
# Получилось:
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
# Добавлен уместный комментарий в строке 145 (см. первую часть задания).

# 4-8. Рассматриваем код решения задачи "Безумный Макс" курса "28 задач":
def MadMax(N, Tele):
    is_not_sorted = True
    while(is_not_sorted):
        is_not_sorted = False     # предполагаем, что массив уже отсортирован
        for i in range(N - 1):
            if Tele[i] > Tele[i+1]:
            # нашли элементы,неупорядоченные по возрастанию, меняем их местами:
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
# Код решения задачи был переписан: вместо рабочего массива использована структура данных "упорядоченный список".
# Комментарии (строки 153, 156, 158, 161, 164) удалены.
# Стало:
def MadMax(N, Tele):
    list_of_values = OrderedList(True)    # упорядоченный список по возрастанию
    for number in Tele:
        list_of_values.add(number)
    result = []
    node = list_of_values.head
    for i in range(N //2):    # формируем "возрастающую" часть результата
        result.append(node.value)
        node = node.next
    stop_value = node.value
    node = list_of_values.tail
    while node.value != stop_value:    # формируем "убывающую" часть результата
        result.append(node.value)
        node = node.prev
    return result
# Добавлены уместные комментарии (строки 177, 182, 187)