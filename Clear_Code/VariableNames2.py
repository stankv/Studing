# 6.1 Более наглядный учет уровней абстракции в именах переменных
# Рассматриваем код решения задачи "146%" курса "28 задач"
# Изменены имена переменных в строках: 7, 11, 14, 20, 23, 37

def MassVote(N, Votes):
    # ищем максимальное значение в массиве (макс. число голосов) и его позицию
    max_number_of_votes = 0    # было vote = 0
    for i in range(len(Votes)):
        if Votes[i] > max_number_of_votes:
            max_number_of_votes = Votes[i]
            candidate_with_max_votes = i    # было number

    # проверяем есть ли еще кандидаты с тем же числом голосов
    candidates_with_same_number_votes = 0    # было count
    for i in range(N):
        if Votes[i] == max_number_of_votes:
            candidates_with_same_number_votes += 1

    # считаем процент голосов за каждого кандидата
    total_number_of_votes = 0    # было sum
    for ani in Votes:
        total_number_of_votes += ani    # 100%
    Percent_of_votes_for_each = []    # было Persent
    for i in range(N):
        value = Votes[i] * 100 / total_number_of_votes
        # округляем получившиеся значения до 3-го знака
        value = int(value * 10000)
        value1 = value // 10
        value2 = value % 10
        if value2 >= 5:
            value1 += 1
        value = value1 / 1000
        Percent_of_votes_for_each.append(value)
    
    
    if candidates_with_same_number_votes == 1 and Percent_of_votes_for_each[candidate_with_max_votes] > 50.0:
        result_of_voting = "majority winner " + str(candidate_with_max_votes + 1)    # было result
    elif candidates_with_same_number_votes == 1 and Percent_of_votes_for_each[candidate_with_max_votes] <= 50.0:
        result_of_voting = "minority winner " + str(candidate_with_max_votes + 1)
    elif candidates_with_same_number_votes > 1:
        result_of_voting = "no winner"

    return result_of_voting

# 6.2 В качестве имён переменных технические термины из информатики.  
# 1). Фильтр Блюма - https://github.com/stankv/Studing/blob/main/Algoritms/BloomFilter1.py
# строка 33: переменная bitmask (битовая маска)

# 2). Код решения задачи "146%" курса "28 задач" - https://github.com/stankv/Studing/blob/main/13_UFO.py
# строка 1 (либо 3): переменная octal (система счисления)

# 3). Код решения задачи "146%" курса "28 задач" - https://github.com/stankv/Studing/blob/main/13_UFO.py
# строка 1 (либо 11): переменная data (здесь - входные данные)

# 4). Очередь - https://github.com/stankv/Studing/blob/main/Algoritms/Queue1.py
# строка 4: переменная (имя массива) queue (очередь)

# 6.3 Имена переменных даны с учётом контекста (функции, метода, класса). 
# 1. класс Liquids (жидкости). Атрибуты (переменные) класса: water, alcohol, acid
# 2. класс Liquids (жидкости). Метод изменения значений температур жидкостей в соответствии с их теплоемкостями temperature()
# переменные метода: temp_water, temp_alcohol, temp_acid
# 3. Функция пересчета температур по разным шкалам temperature_recalculate().
# переменные функции: temp_Celsius, temp_Fahrenheit, temp_Kelvin

# 6.4 Переменные, длины которых не укладываются в 8-20 символов.
# Рассматриваем код решения задачи "Миссия невыполнима: Красный портфель" курса "28 задач"
# Изменены имена переменных в строках: 71, 87( и 90), 101, 121, 135
def TheRabbitsFoot(s, encode):
    def Coder(s):
        # удаляем из строки все пробелы
        line_no_spaces = ""    # было s1
        for ani in s:
            if ani != " ":
                line_no_spaces = line_no_spaces + ani
        # вычисляем размер матрицы
        N = len(line_no_spaces)
        n = pow(N, 0.5)
        row = int(n)
        column = int(n * 10) - row * 10
        if column == 0:
            column = row
        if (row * column) < N:
            while((row * column) < N):
                row += 1
        N = row * column    # размер рабочей матрицы
        # дополняем строку пробелами чтобы влезала полностью в массив
        line_with_spaces = line_no_spaces    # вместо s1 введена новая переменная
        if len(line_no_spaces) < N:
            for i in range(N - len(line_no_spaces)):
                line_with_spaces = line_with_spaces + " "
        # формируем матрицу
        Matrix = []
        count = 0
        for i in range(row):
            b = []
            for j in range(column):
                b.append(line_with_spaces[count])
                count += 1
            Matrix.append(b)
        # шифруем данные
        encrypted_line = ""    # было s1
        for i in range(column):
            for j in range(row):
                if Matrix[j][i] == " ":
                    encrypted_line += ""
                else:
                    encrypted_line += Matrix[j][i]
            if i < (column - 1):
                encrypted_line += " "
        return encrypted_line

    def Decoder(s):
        # декодируем строку s
        S = s.split()    # разбиваем строку на слова
        # удаляем из строки все пробелы
        line_no_spaces = ""    
        for ani in s:
            if ani != " ":
                line_no_spaces = line_no_spaces + ani
        N = len(S[0])    # "длина" цикла по буквам слова
        decrypted_line = ""    # расшифрованная строка, было s1
        i = 0
        k = 0
        L = len(line_no_spaces)
        while(i < N):
            for ani in S:
                decrypted_line = decrypted_line + ani[i]
                k = k + 1
                if k == L:
                    break
            i = i + 1
        return decrypted_line

    if encode == True:
        result_of_solving = Coder(s)    # было result
    elif encode == False:
        result_of_solving = Decoder(s)
    return result_of_solving