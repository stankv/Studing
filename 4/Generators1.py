# ГЕНЕРАТОРЫ. "Одновременная" работа произвольного числа генераторов.
# N - число "одновременно" работающих генераторов
# L - массив, значения которого есть n для функции long_process(id, n)
import random

def Generators(L):
    # генератор
    def long_process(id, n):
        sum = 0
        for x in range(n):
            sum += x
            print(id, sum)
            if x < n-1:
                yield
            else:
                yield sum

    # "инициализация" и запуск генераторов
    N = len(L)    # количество запускаемых генераторов
    ID = []
    Id = []
    R = {}
    for i in range(N):
        IDn = "ID" + str(i)
        ID.append(IDn)
        IDk = long_process(IDn, L[i])
        Id.append(IDk)
        R[IDn] = None

    for j in range(max(L)):
        for i in range(N):
            if R[ID[i]] is None: 
                R[ID[i]] = next(Id[i])

    # ожидаем завершения выполнения всех генераторов
    proc_running = True
    while(proc_running):
        proc_running = False
        for r in range(N):
            if R[ID[r]] == None:
                proc_running = True
                break    # сразу выходим из for если данный процесс продолжается
    print(R)

N0 = random.randint(3, 10)
L0 = []
for i in range(N0):
    L0.append(random.randint(1, 10))    # создаем входные данные - массив случайных целых чисел случайной длины
Generators(L0)