# РЕКУРСИВНАЯ ФУНКЦИЯ
# Вычисление суммы цифр числа N

def Calculation(Number, sum):
    if Number == 0:
        return sum
    else:
        sum += (Number % 10)
        return Calculation(Number // 10, sum)

def SumOfDigitsOfNumber(N):
    starting_value = 0
    return Calculation(N, starting_value)

number = int(input("Введите число:"))
print("Сумма цифр =", SumOfDigitsOfNumber(number))