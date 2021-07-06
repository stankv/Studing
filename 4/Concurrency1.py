# ОДНОВРЕМЕННЫЕ ПРОЦЕССЫ
# Функция получает на вход массив вещественных чисел L и количество процессов N. Каждый процесс суммирует свой
# "участок" массива. Затем суммы складываются и дают итоговую сумму чисел всего массива.

import random
import time
from threading import Thread

def Concurrency(N, L):
    def Calculate(id, Spisok, res):
        sum = 0
        for ani in Spisok:
            sum += ani
            time.sleep(0.05)
        res[id] = sum

    # Разбиваем массив L на N частей, создаем 2-мерный массив из этих частей
    k = len(L) // N
    if k >= 1:    # число операций в каждом потоке должно быть не меньше 1
        N1 = 0
        N2 = k
        S = []
        for i in range(N):
            b = []
            for j in L[N1:N2]:
                b.append(j)
            S.append(b)
            if i < N - 2:
                N1 += k
                N2 += k
            elif i == N - 2:
                N1 += k
                N2 = len(L)

        # Запускаем N процессов счета (N функций Calculate)
        results = {}    # результаты работы процессов запишем в словарь
        Threads = []
        i = 1    # - id процесса
        for submassiv in S:
            t = Thread(target=Calculate, name="Thread", args=(i,submassiv,results))
            Threads.append(t)
            t.start()
            i += 1
        time.sleep(5.0)
        # Если мы хотим подождать завершения каждого процесса, то с цикла ниже снять комментирование, и закомментить верхнюю строку
        #for t in Threads:
            #t.join()
        success = sum(results.values())
        return success
    else:
        return sum(L)