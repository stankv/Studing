# РЕКУРСИВНАЯ ФУНКЦИЯ
# Вычисление суммы цифр числа N

def SumOfDigitsOfNumber(N):
    global sum
    if N == 0:
        return sum
    else:
        digit = N % 10
        sum += (N % 10)
        return SumOfDigitsOfNumber(N // 10)

sum = 0
number = int(input("Введите число:"))
print("Сумма цифр =", SumOfDigitsOfNumber(number))