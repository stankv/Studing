def PatternUnlock(N, hits):
    subS = ["62", "26", "27", "72", "29", "92", "24", "42", "15", "51", "53", "35", "18", "81", "38", "83"]
    hits1 = []
    # преобразуем входной массив чисел в строку
    for i in range(N):
        hits1.append(str(hits[i]))
    hits1 = "".join(hits1)
    
    # поиск подстрок в строке
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