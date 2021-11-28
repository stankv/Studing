# Время связывания переменных

# Рассматриваем код решения задачи "Делаем национальный редактор "Лапоть"" курса "28 задач"
# https://github.com/stankv/Studing/blob/main/20_BastShoe.py
# Это единственная в курсе задача, в которой для решения пришлось применить глобальные переменные.
# Ниже изначальный код решения задачи:

# ТЕКСТОВЫЙ РЕДАКТОР "ЛАПОТЬ"

# глобальные переменные
S = []    # массив получившихся строк
current_stroka = ""    # текущая строка
index_S = -1   # индекс текущей строки в массиве
flag = False

def BastShoe(command):

    global S    # массив получившихся строк
    global current_stroka    # текущая строка
    global index_S    #  индекс текущей строки в массиве
    global flag

    # удаляем пробелы в начале строки если они есть
    commandf = command.lstrip()
    # из введенной команды выделяем саму команду и операнд
    operation = ""
    stroka = ""
    if len(commandf) == 1:
        stroka = ""
        operation = (commandf[0])
    elif len(commandf) > 1:
        for i in range(len(commandf)):
            if commandf[i] != " ":
                operation += commandf[i]
            elif commandf[i] == " ":
                k = i + 1
                break
        for i in range(k, len(commandf)):
            stroka += commandf[i]

    # выполняем команды
    # добавление строки к строке
    if operation == "1":
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
    # удаление символов из конца строки
    elif operation == "2":
        stroka = stroka.rstrip()    #    удаляем пробелы справа если они есть
        try:
            N = int(stroka)             # исключение, если stroka не есть число -> ValueError - возвращаем пустую строку
        except ValueError:
            return ""
        if flag:
            current_stroka = S[index_S]
            if len(current_stroka) <= N:
                current_stroka = ""
                S = []
                S.append(current_stroka)
                index_S = 0
                flag = False
            else:
                current_stroka = S[index_S]
                S = []
                S.append(current_stroka)
                current_stroka = current_stroka[:-N]
                S.append(current_stroka)
                flag = False
        else:
            current_stroka = S[index_S]
            if len(current_stroka) <= N:
                current_stroka = ""
                S.append(current_stroka)
                index_S = index_S + 1
            else:
                current_stroka = current_stroka[:-N]
                S.append(current_stroka)
                index_S = index_S + 1
        return current_stroka

    # выдать i-й символ текущей строки
    elif operation == "3":
        stroka = stroka.rstrip()    # удаляем пробелы справа если они есть
        try:
            I = int(stroka)             # исключение, если stroka не есть число -> ValueError - возвращаем пустую строку
        except ValueError:
            return ""
        if len(current_stroka) < (I + 1) or (I + 1) < 0:
            symbol = ""
        else:
            current_stroka = S[index_S]
            symbol = current_stroka[I]
        return symbol
    # операция Undo
    elif operation == "4":
        if len(S) == 0:
            current_stroka = ""
            index_S = -1   
        elif len(S) == 1:
            index_S = 0
            current_stroka = S[index_S]
        elif len(S) > 1:
            index_S = index_S - 1
            if index_S < 0:
                index_S = 0
            current_stroka = S[index_S]
            flag = True
        return current_stroka
    # операция Redo
    elif operation == "5":
        if index_S == (len(S) - 1):
            current_stroka = S[index_S]
        elif index_S < (len(S) - 1):
            index_S = index_S + 1
            current_stroka = S[index_S]
            if index_S == (len(S) - 1):
                flag = False
        return current_stroka
    else:
        return current_stroka

# 1. Максимально раннее связывание: здесь использованы глобальные переменные, "запоминающие состояние". 
# Поэтому они сразу объявлены и инициализированы конкретными значениями:
S = []    # массив получившихся строк
current_stroka = ""    # текущая строка
index_S = -1   # индекс текущей строки в массиве
flag = False
# Как было показано в прошлом занятии, для сужения области видимости этих переменных их можно сделать полями класса:
class main_variables:
    def __init__(self):
        self.S = []
        self.current_stroka = ""
        self.index_S = -1
        self.flag = False
# В обоих случаях, в виду специфики логики кода решения задачи, эти переменные (или поля класса) должны быть объявлены 
# и инициализированы конкретными (начальными) значениями.

# 2. Связывание во время компиляции кода: те значения, которые задаются глобальным переменным (либо полям класса) 
# при их инициализации, затем не раз присваиваются им снова по ходу выполнения программы, например:
S = []                 #строки 49, 71, 77
current_stroka = ""    # строки 45, 70, 85, 110
index_S = -1           # строка 111
flag = False           #строки 54, 74, 81, 130
# Поэтому для повышения гибкости кода можно создать константы:
EMPTY_ARRAY = []
EMPTY_STRING = ""
UNACCEPTABLE_INDEX = -1
NO = False
YES = True
# И по ходу программы в соответствующих строках делать присвоение глобальным переменных соответствующих значений:
S = EMPTY_ARRAY
current_stroka = EMPTY_STRING
index_S = UNACCEPTABLE_INDEX
flag = NO    # это для примера, применение такого хода в программе скорее всего излишне.

# 3. Связывание во время выполнения программы: В программе используется строковая переменная operation, значение 
# которой "вычисляется" в строках 23-34. Значения этой переменной могут быть только "1", "2", "3", "4" и "5". Если вдруг 
# какое-то другое (т.е. некорректное) значение, то редактор "Лапоть" ничего не делает. Т.о. связывание этой переменной с 
# конкретным значением происходит во время выполнения программы.

# Другой пример - строковая переменная command, подающаяся на вход функции BastShoe(command) - строка 16. 
# Эта переменная получает свое значение от пользователя путем ввода с клавиатуры:
instruction = input(">> ")
BastShoe(instruction)
# Т.о. она тоже "связывается" со значением, заданным пользователем, непосредственно во время работы программы.