def UFO(N, data, octal):
    # выбор системы счисления по флагу
    if octal:
        n = 8
    else:
        n = 16

    # перевод чисел массива в десятичную систему
    Res = []
    for i in range(N):
        Res.append(int(str(data[i]), n))
    
    return Res