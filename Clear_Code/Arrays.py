# Массивы
# Приведите 5 примеров вашего кода, где вместо массивов можно использовать более безопасные структуры данных, 
# или же работа с самими массивами может выполняться без их прямой индексации. 

# 1. Рассматриваем код решения задачи "Поездка на мотоцикле" курса "28 задач"
def odometer(N):
    time_current = 0        # время движения на конкретном (текущем) участке пути
    time_elapsed = 0        # полное время движения до текущего участка пути
    distance_travelled = 0  # общее пройденное расстояние
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

# В цикле имеет место прямая индексация при работе с массивом N[]. Чтобы избежать прямой индексации, можно 
# переписать цикл так:
count = 0
loop_counter = 0
for  ani in N:
    if loop_counter % 2 == 0:
        velocity_current = ani
    else:
        time_current = ani - time_elapsed
            time_elapsed = ani
        count = count + 1
        if count % 2 == 0 and count != 0:
            distance_travelled += velocity_current * time_current
    loop_counter += 1
# Т.о. отсутствует прямая индексация, цикл полностью проходит по всем элементам итерируемого объекта (массива) 
# без возможности возникновения проблем при обращении к граничным элементам массива, ошибка потери единицы автоматически
# исключается.

# 2. Рассматриваем код решения задачи "Экономим тонер" курса "28 задач":
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
# Имеет место прямая индексация при работе с массивом TableSymbols[]. Чтобы этого избежать, можно использовать вместо 
# этого массива структуру данных словарь:
    TableSymbols = {" ": 0, "!": 9, "\"": 6, "#": 24, "$": 29, \
# .....................................
                    "z": 19, "{": 18, "|": 12, "}": 18, "~": 9}
# Тогда код решения (строки 77-91) можно переписать так:
    res = 0
    LineWork = raw(Line)
    for ani in LineWork:
        res += TableSymbols.get(ani, 23)
    return res
# При этом переменные N и switch больше не нужны и сам код заметно сократился, а скорость работы возросла за счет 
# использования словаря вместо массива. И можно вообще обойтись без кода строк 42-63. Т.о. весь код решения задачи 
# можно переписать очень коротко и лаконично так:
def PrintingCosts(Line):
    TableSymbols = {" ": 0, "!": 9, "\"": 6, "#": 24, "$": 29, \
    # .....................................
                    "z": 19, "{": 18, "|": 12, "}": 18, "~": 9}
    result = 0
    for symbol in Line:
        result += TableSymbols.get(symbol, 23)
    return result

# 3. Рассматриваем код решения задачи "Безумный Макс" курса "28 задач":
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

# Имеет место прямая индексация при работе с массивом Tele[]. Чтобы этого избежать, а также с учетом 
# условий задачи, можно использовать вместо этого массива структуру данных упорядоченный список, например, 
# его реализацию на основе двунаправленного связанного списка - 
# https://github.com/stankv/Studing/blob/main/Algoritms/OrderedList1.py. Тогда код решения задачи перепишется так:
def MadMax(N, Tele):
    list_of_values = OrderedList(True)    # объявляем упорядоченный список по возрастанию
    for ani in Tele:
        list_of_values.add(ani)    # формируем упорядоченный список из элементов входного массива
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

# 4. Рассматриваем код решения задачи "Шопоголики" курса "28 задач":
def MaximumDiscount(N, price):
    # сортируем массив по убыванию
    sorted_list = sorted(price, reverse = True)
    # каждый третий предмет даст макисмальную скидку при покупке этих 3-х предметов
    discount = 0
    for i in range(2, N, 3):
        discount += sorted_list[i]
    return discount

# Вместо массива sorted_list[] можно опять же использовать структуру упорядоченный список, код перепишется так:
def MaximumDiscount(N, price):
    sorted_list = OrderedList(False)
    for ani in price:
        sorted_list.add(ani)    # формируем упорядоченный по убыванию список из элементов входного массива
    discount = 0
    node = sorted_list.head
    count = 1
    for i in range(N):
        if count == 3:
            discount += node.value
            count = 1
        else:
            count += 1
        node = node.next
    return discount

# 5. Рассматриваем код решения задачи "Искусственный интеллект для Оксаны" курса "28 задач":
def SumOfThe(N, data):
    # считаем сумму всего массива
    full_sum = 0
    for i in range(N):
        full_sum = full_sum + data[i]
    # ищем число, равное сумме всех элементов массива без него
    result = 0
    for i in range(N):
        if (full_sum - data[i]) == data[i]:
            result = data[i]
            break
    return result

# Вместо работы с массивом data[] и его значениями напрямую по индексу, можно использовать
# структуру данных простой связанный список. Реализация однонаправленного связанного списка - 
# https://github.com/stankv/Studing/blob/main/Algoritms/LinkedList1.py
# Тогда код решения задачи можно переписать так:
def SumOfThe(N, data):
    full_sum = sum(data)    # считаем сумму всего массива
    linked_list = LinkedList()
    for ani in data:
        linked_list.add_in_tail(Node(ani))
    node = linked_list.head
    while node is not None:
        if (full_sum - node.value) == node.value:
            return node.value
        node = node.next