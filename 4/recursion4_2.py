# Проверка, является ли строка палиндромом (используем стек)
def CheckPalindrom(stroka):
    stack = list(stroka.replace(' ', ''))    # удаляем пробелы из строки и заносим ее в стек
    N = len(stack) // 2
    result = True
    for i in range(N):
        if stack[i] == stack.pop():
            continue
        else:
            result = False
            return result
    return result

str1 = "а роза упала на лапу азора"
if CheckPalindrom(str1):
    print("Строка является палиндромом")
else:
    print("Строка НЕ является палиндромом")