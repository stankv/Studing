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