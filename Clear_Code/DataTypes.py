# Типы данных

# I. Общие рекомендации.
# 1. Выполняйте преобразования типов понятно -- а лучше вообще никогда не приводите значения одних типов к другим. 
# При преобразовании типов могут возникать ошибки при неправильно заданных аргументах. Например float("2/5 stroka"), 
# int("abc"). Преобразование int(2.5) отбросит дробную часть.
# Преобразования, которые не вызовут ошибки компилятора:
# int -> float
# int -> str
# float -> str
# bool -> int
# bool -> str
# bool -> float
# int, float или str -> bool
# для определения какой тип можно использовать ф-ю type(), например type (6 / 3)

# 2. Избегайте сравнений значений разных типов. 
# При сравнении значений разных типов могут возникать ошибки TypeError, например:
x = 'abc'
y = 5.0
print(x >= y)    # TypeError: '>=' not supported between instances of 'str' and 'float'
# При этом if x == y: не вызовет ошибки.

# 3. Обращайте внимание на предупреждения вашего компилятора (включите все предупреждения по максимуму). 
# Включение предупреждений компилятора можно сделать командой python -W 
# см. https://docs.python.org/3/using/cmdline.html#cmdoption-W
# Предупреждениями также можно управлять с помощью переменной среды PYTHONWARNINGS и из программы Python 
# с помощью модуля предупреждений warnings. 

# 4. Каждый раз, когда вы пользуетесь символом деления (/ в большинстве языков), думайте о том, может ли в знаменателе 
# оказаться 0. Если такая возможность существует, напишите код, предупреждающий появление ошибки деления на 0.
x = 10
y = 0
if y != 0:
    z = x / y
else:
    print('Division by zero!') 
# или лучше так:
try:
    z = x / y
except ZeroDivisionError:
    print('Division by zero in #39')
# Ошибка также может возникать при использовании операций: /, //, %

#--------------------------------------------------------------------------------------------------------------------------
# II. Целые числа
# 5. Проверяйте целочисленность операций деления (используйте подходящие операции деления). 
print(6 / 3)      # = 2.0, тип float!
print(6 // 3)     # = 2, тип int!
print(7 / 3)      # = 2.3333333333333335, тип float!
print(7 / -3)     # = -2.3333333333333335
print(7 // 3)     # = 2, тоже тип int
print(7 % 3)      # = 1
print(-7 // 3)    # = -3, а не -2
print(-7 % 3)     # = 2, а не -2
print(7 // -3)    # = -3
print(7 % -3)     # = -2
print(-7 // -3)   # = 2 
print(- 7 % -3)   # = -1
# Т.о. при использовании отрицательных операндов легко сделать ошибку в логике кода.

# 6. Проверяйте возможное переполнение целых чисел.
# 7. Проверяйте на переполнение промежуточные результаты вычислений внутри выражений. 
# В Python реализована арифметика длинных чисел, и проблем с переполнением не возникает. Но при 
# использовании библиотек Numpy, Pandas, Pydata и Sys это возможно и бывает. 
# Пример ниже, демонстрирующий это, найден в интернете:
import numpy as np
a = np.array([3095693933], dtype=int)  
s = np.sum(a)
print(s)            # 3095693933
print(s * s)        # -8863423146896543127
print(type(s))      # numpy.int64
py_s = int(s)
print(py_s * py_s)  # 9583320926813008489

#--------------------------------------------------------------------------------------------------------------------------
# III. Вещественные числа 
# 8. Избегайте сложения и вычитания слишком разных по величине чисел. 
x = 0.1 + 0.1 + 0.1    # x = 0.30000000000000004, а не 0.3
y = x + 0.0000000000000009    # y = 0.30000000000000093, вместо 0.0000000000000013

# 9. Избегайте сравнений на равенство.
x = 0.1 + 0.1 + 0.1    # x = 0.30000000000000004, вместо 0.3
x == 0.3    # = False

# 10. Предупреждайте и учитывайте ошибки округления. 
round(.1, 1) + round(.1, 1) + round(.1, 1) == round(.3, 1)    # = False

# 11. Измените тип вещественной переменной на тип с большей точностью. 
# 12. Если вы используете числа с одинарной точностью, замените их числами с двойной точностью и т. д. 
# В Python по умолчанию для float используется двойная точность, т.е. тип double, дающий 16 знаков 
# после запятой. Для повышения точности можно использовать модуль Decimal, в котором можно задавать точность:
from decimal import *
getcontext()
getcontext().prec = 6
Decimal(1) / Decimal(7)    # = Decimal('0.142857')

getcontext().prec = 28
Decimal(1) / Decimal(7)    # = Decimal('0.1428571428571428571428571429')
# Повышая точность мы увеличиваем время работы программы.
# Decimal "не дружит" с float и complex.

# Также можно использовать модуль fractions, который дружит с float, поскольку для 
# отображения чисел использует дроби (отношение рациональных чисел). Но не может быть аргументом
# некоторых ф-й, например log10.
from fractions import Fraction
Fraction(16, -10)    # Fraction(-8, 5)
Fraction(123)        # Fraction(123, 1)
Fraction()           # Fraction(0, 1)
Fraction('3/7')      # Fraction(3, 7)
Fraction('1.414213 \t\n')    # Fraction(1414213, 1000000)
Fraction('-.125')    # Fraction(-1, 8)
Fraction('7e-6')    # Fraction(7, 1000000)
Fraction(1.1)    # Fraction(2476979795053773, 2251799813685248)

from decimal import Decimal
Fraction(Decimal('1.1'))    # Fraction(11, 10)

# 13. Измените в коде места, где используются значения с плавающей запятой, на целые значения, если это возможно.
# Для этого можно использовать модуль fractions, или разбивать число на 2 целых - отдельно целую часть и отдельно дробную. 
# Количество кода немного увеличится, но поможет избежать ошибок, особенно при сравнении чисел.
# Разделение числа на целую и дробную части:
x = 3.1415
x_str = str(x)
celoe = []
drobnoe = []
k = 0
for i in x_str:
    if i == '.':
        k = 1
        continue
    if k == 0:
        celoe.append(i)
    elif k == 1:
        drobnoe.append(i)
celoe = int("".join(celoe))
drobnoe = int("".join(drobnoe))
print('celoe=', celoe, "drobnoe=", drobnoe)

# ------------------------------------------------------------------------------------------------------------------------
# IV. Строки и символы 
# 14. Избегайте магических символов и строк -- используйте константы. 
# Например, в коде решения задачи "Делаем национальный редактор "Лапоть"" курса "28 задач"
# https://github.com/stankv/Studing/blob/main/20_BastShoe.py
# значения операций ("1", "2" и т.д.) можно присвоить константам ADD_TO_END_STRING = '1', 
# DEL_CHARACTERS = '2', GET_CHARACTER = '3', UNDO = '4', REDO = '5'

# 15. Узнайте, как ваш язык и система поддерживают Unicode, и перейдите на этот формат. 
# Для преобразования строки в UTF-8 можно использовать префикс u: u'abc xyz'
# Также для преобразования кодировки к нужной используются методы encode('utf-8') и decode('utf-8'),
# пример - строка 39 https://github.com/stankv/Studing/blob/main/4/TCPchat_server.py
client.send('NICK'.encode('utf-8'))    # отправляем клиенту запрос его имени/ника

# 16. Разработайте стратегию интернационализации/локализации текстовых сообщений в вашем
# коде (делайте это в самый ранний период создания программы). 
# Модуль gettext обеспечивает интернационализацию и локализация службы для ваших модулей Python и приложений. 
from gettext import *
gettext.gettext("Message") # Возвращает локализованный перевод сообщения на основе 
# текущего глобального каталога домена, языка и языкового региона.

#---------------------------------------------------------------------------------------------------------------------------
# Логические переменные 
# 17. Активнее используйте логические переменные для повышения читабельности программы. 
# Пример: код решения задачи "Мастер ключей" курса "28 задач" https://github.com/stankv/Studing/blob/main/28_Keymaker.py
# Вместо значений "0" и "1" будет более наглядно использовать False и True соответственно.