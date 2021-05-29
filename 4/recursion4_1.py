# Проверка, является ли строка палиндромом (без использования рекурсии)
def CheckPalindrom(stroka):
    stroka1 = stroka.replace(' ', '')    # удаляем пробелы из строки
    result = True
    N = len(stroka1) // 2
    for i in range(N):
        if stroka1[i] == stroka1[-i - 1]:
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