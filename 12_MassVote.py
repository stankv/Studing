def MassVote(N, Votes):
    # ищем максимальное значение в массиве и его позицию
    vote = 0
    for i in range(len(Votes)):
        if Votes[i] > vote:
            vote = Votes[i]
            number = i

    # проверяем есть ли еще кандидаты с тем же числом голосов
    count = 0
    for i in range(N):
        if Votes[i] == vote:
            count += 1

    # считаем процент голосов за каждого кандидата
    sum = 0
    for ani in Votes:
        sum += ani    # - 100%
    Persent = []
    for i in range(N):
        value = Votes[i] * 100 / sum
        # округляем получившиеся значения до 3-го знака
        value = int(value * 10000)
        value1 = value // 10
        value2 = value % 10
        if value2 >= 5:
            value1 += 1
        value = value1 / 1000
        Persent.append(value)
    
    
    if count == 1 and Persent[number] > 50.0:
        result = "majority winner " + str(number + 1)
    elif count == 1 and Persent[number] <= 50.0:
        result = "minority winner " + str(number + 1)
    elif count > 1:
        result = "no winner"

    return result