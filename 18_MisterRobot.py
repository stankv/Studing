# СОРТИРОВКА МАССИВА ПО ВОЗРАСТАНИЮ ПУТЕМ ЦИКЛИЧЕСКИХ ПЕРЕСТАНОВОК 3-Х БЛИЖАЙШИХ ЧИСЕЛ
# Возвращает True если массив отсортирован, и False если невозможно отсортировать.
def MisterRobot(N, data):
    flag = False    # - элементы массива не отсортированы по возрастанию
    while(not flag):
        for i in range(N - 2):
            if data[i] < data[i + 1] and data[i + 1] < data[i + 2]:
                flag = True
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
                        flag = False
                        return flag
        # проверяем есть ли неотсортированные элементы в массиве
        flag = True
        for j in range(N - 1):
            if data[j + 1] < data[j]:
                flag = False
                break
    return flag