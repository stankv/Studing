# РЕКУРСИВНАЯ ФУНКЦИЯ
# Возведение числа N в степень M
def powernumber(N, M):
    if M == 1:    # базовое условие рекурсии
        return N
    else:
        return N * powernumber(N, M - 1)