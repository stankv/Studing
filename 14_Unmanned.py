def Unmanned(L, N, track):
    
    T = 0     # пройденный путь (время)
    Distance1 = 0
    # движемся по отрезкам пути (от сфетофора к светофору)
    # считываем данные о ближайшем светофоре
    for i in range(N):
        Distance2 = track[i][0]
        red = track[i][1]
        green = track[i][2]
        # едем или стоим на светофоре ( и сколько стоим)
        Distance = Distance2 - Distance1
        T = T + Distance
        stop = T % (red + green)
        if stop >= red:    # красный перестал гореть
            stop = 0
        else:
            stop = red - stop    # красный горит и будет еще гореть столько моментов времени
        T = T + stop
        Distance1 = Distance2
    # все светофоры проехали, остался прямой участок пути до финиша
    T = T + (L - Distance1)
    return T