# ИСПОЛЬЗОВАНИЕ РЕКУРСИВНОЙ ФУНКЦИИ
# Проверка, является ли строка палиндромом
def CheckPalindrom(stroka):

    def Palindrome(Spisok):
        if len(L) <= 1:    # количество букв строки может быть как четным, так и нечетным
            return True    # тогда для базового условия len(L) == 0, либо == 1
        else:
            symbol_one = L.pop(0)
            symbol_end = L.pop()
            if symbol_one == symbol_end:
                return Palindrome(L)
            else:
                return False

    # строку "переведем" в массив символов для возможности использования функции pop(), удаляя все пробелы
    L = []
    for i in range(len(stroka)):
        if stroka[i] == " ":
            continue
        else:
            L.append(stroka[i])
    
    if Palindrome(L):
        return True
    else:
        return False

str1 = "а роза упала на лапу азора"
if CheckPalindrom(str1):
    print("Строка является палиндромом")
else:
    print("Строка НЕ является палиндромом")