# ИСПОЛЬЗОВАНИЕ РЕКУРСИВНОЙ ФУНКЦИИ
# Нахождение второго максимального числа в списке 
# (с учётом, что максимальных может быть несколько, если они равны)
def SecondMaxNumber(Spisok):
    a = max(Spisok)
    Spisok.pop(Spisok.index(a))
    b = max(Spisok)
    if a != b:
        return b
    else:
        return SecondMaxNumber(Spisok)

L = [1,9,2,3,9,4,5,6,7,8,9]
print(SecondMaxNumber(L))