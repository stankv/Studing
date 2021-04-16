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