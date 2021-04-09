def MadMax(N, Tele):
    xchange = True 
    while(xchange):
        xchange = False # предполагаем, что массив уже отсортирован
        for i in range(N - 1):
            if Tele[i] > Tele[i+1]:
            # нашли элементы,
            # неупорядоченные по возрастанию:
            # меняем их местами:
                Tele[i], Tele[i+1] = Tele[i+1], Tele[i]
            # цикл проверки массива надо продожить снова:
                xchange = True
                
    # меняем местами срединный элемент и последний (наибольший)
    Tele[N // 2 ], Tele[N - 1] = Tele[N - 1], Tele[N // 2]
   
    # с середины сортируем элементы по убыванию   
    xchange = True
    while(xchange):
        xchange = False
        for i in range((N // 2) + 1, N - 1):
            if Tele[i] < Tele[i+1]:
                Tele[i + 1], Tele[i] = Tele[i], Tele[i + 1]
                xchange = True
    return Tele