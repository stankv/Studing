# ПРИМЕР ПРИЛОЖЕНИЯ С GUI. ИСПОЛЬЗОВАНИЕ БИБЛИОТЕКИ TKINTER.
# РЕДАКТОР ДЛЯ ОТЧЕТОВ С КАЛЬКУЛЯТОРОМ.
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter.constants import BOTH, END, INSERT, LEFT
from tkinter import colorchooser

# ФУНКЦИИ МЕНЮ -----------------------------------------------------------------------------------------------------------
FILE_NAME = tk.NONE

# Ф-я создания нового файла
def NewFile():
    global FILE_NAME
    FILE_NAME = 'Untitled'
    mytext.delete('1.0', tk.END)    # просто очищаем содержимое текстового поля

# Ф-я открытия файла
def OpenFile():
    global FILE_NAME
    inp = askopenfile(mode='r')
    if inp is None:
        return
    FILE_NAME = inp.name
    data = inp.read()
    mytext.delete('1.0', tk.END)
    mytext.insert('1.0', data)

# Ф-я сохранения файла
def SaveFile():
    data = mytext.get('1.0', tk.END)    # переменная data получает весь текст текстового поля
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()

# Ф-я сохранения файла как...
def SaveAs():
    out = asksaveasfile(mode='w', defaultextension='txt')
    data = mytext.get('1.0', tk.END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror(title="Ошибка!", message='Ошибка при сохранении файла!')

# Ф-я вывода в отдельном окне информации о программе
def About():
    messagebox.showinfo("О программе", "Редактор для отчетов с калькулятором.\n\nВерсия 1.0\n\nАвтор Stan Korj")

# Ф-я закрытия приложения
def Closing():
    if messagebox.askokcancel("Выход из программы", "Хотите выйти из программы?"):
        root.destroy()
# ------------------------------------------------------------------------------------------------------------------------

# ФУНКЦИИ КАЛЬКУЛЯТОРА ----------------------------------------------------------------------------------------------------

# Ф-я добавления цифровых кнопок калькулятора
def make_digit_button(digit):
    return tk.Button(lbFr2, text=digit, bd=5, font=('Arial', 13), command=lambda: add_digit(digit))

# Ф-я добавления кнопок операций калькулятора
def make_operation_button(operation):
    return tk.Button(lbFr2, text=operation, bd=5, font=('Arial', 13), fg='red', command=lambda: add_operation(operation))

# Ф-я добавления кнопки вычисление (т.е. "=")
def make_calc_button(operation):
    return tk.Button(lbFr2, text=operation, bd=5, font=('Arial', 13), fg='red', command=calculate)

# Ф-я добавления кнопки очистки текст. поля калькулятора
def make_clear_button(operation):
    return tk.Button(lbFr2, text=operation, bd=5, font=('Arial', 13), fg='red',command=clear)

# Ф-я добавления кнопки "Вставить в текст"
def insert_result_button(operation):
    return tk.Button(lbFr2, text=operation, height=3, bd=5, font=('Arial', 13), fg='blue', command=insert_text)

# Ф-я обработки ввода с клавиатуры (работает при наличии строки root.bind('<Key>', press_key))
def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-/*':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()

# Ф-я печатает цифры нажимаемых кнопок 
def add_digit(digit):
    value = calc.get()    # получаем содержимое текст. поля
    if value[0] == '0' and len(value) == 1:   # если там 0, то удаляем его
        value = value[1:]
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)    # очищаем текстовое поле
    calc.insert(0, value + digit)    # вставляем в текст. поле результат
    calc['state'] = tk.DISABLED

# Ф-я добавления операции
def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-/*':    # если ранее была введена операция и добавлена новая, то удаляем старую
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value = calc.get()
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)
    calc['state'] = tk.DISABLED

# Ф-я вычисления
def calculate():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value + value[:-1]
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание!', 'Вводить можно только цифры!')
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showerror('Ошибка!', "На ноль делить нельзя!")
        calc.insert(0, 0)
    calc['state'] = tk.DISABLED

# Ф-я очистки текст. поля калькулятора (нажатие клавиши "C")
def clear():
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, 0)
    calc['state'] = tk.DISABLED

# Ф-я вставки в текст результатов расчета калькулятора
def insert_text():
    value1 = calc.get()
    mytext.insert('insert', value1)    # вставка в место где стоит курсор

#-------------------------------------------------------------------------------------------------------------------------
# ФУНКЦИИ ОКНА НАСТРОЕК РЕДАКТОРА ----------------------------------------------------------------------------------------
# Ф-я создания дочернего окна - настройки для редактора
def winSet():
    def choose_color():
        return colorchooser.askcolor()[1]    # возвращает выбранный цвет

    winSetting = tk.Toplevel()    # создаем дочернее окно
    winSetting.title("Настройки редактора")
    winSetting.geometry('400x300+200+200')
    # Создаем вкладки
    tab_control = ttk.Notebook(winSetting)
    # вкладка "Шрифт". О настройке шрифтов https://www.delftstack.com/ru/howto/python-tkinter/how-to-set-font-of-tkinter-text-widget/
    tab1 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='  Шрифт  ')
    tab_control.pack(expand=1, fill='both')
    lbl1 = tk.Label(tab1, text="Шрифт текста:  ")
    lbl1.grid(row=3, column=0, padx=10, pady=20)
    fonts = ("Arial", "Times New Roman", "Verdana", "Tahoma")
    combo_font = ttk.Combobox(tab1, values=fonts)
    combo_font.current(0)    # шрифт по умолчанию = индексу элемента в кортеже
    combo_font.grid(row=3, column=1, padx=10, pady=20)
    lbl2 = tk.Label(tab1, text="Размер шрифта:")
    lbl2.grid(row=5, column=0, padx=10, pady=20)
    font_size_default = tk.StringVar(root)    # устанавливаем значение размера шрифта по умолчанию
    font_size_default.set("12")
    combo_size = tk.Spinbox(tab1, from_=8, to=72, width=5, textvariable=font_size_default)
    combo_size.grid(row=5, column=1, padx=10, pady=20, sticky='w')
    
    # вкладка "Цвет"
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab2, text='  Цвет  ')
    tab_control.pack(expand=1, fill='both')
    lbl3 = tk.Label(tab2, text="Цвет текста:")
    lbl3.grid(row=1, column=0, padx=10, pady=20)
    color_field1 = tk.Canvas(tab2, width=50, height=30, bg='light green')
    color_field1.grid(row=1, column=1, pady=20, sticky='w')
    color_field1.create_rectangle(0, 0, 50, 30, fill='yellow', outline='white', width=3)
    btn2 = tk.Button(tab2, text="Выбрать", command=choose_color)
    btn2.grid(row=1, column=3, padx=10, pady=20)
    #color_field.create_rectangle(0, 0, 50, 30, fill=choose_color(), outline='white', width=3)
    lbl4 = tk.Label(tab2, text="Цвет фона:")
    lbl4.grid(row=2, column=0, padx=10, pady=20)
    color_field2 = tk.Canvas(tab2, width=50, height=30, bg='light green')
    color_field2.grid(row=2, column=1, pady=20, sticky='w')
    color_field2.create_rectangle(0, 0, 50, 30, fill='black', outline='white', width=3)
    btn3 = tk.Button(tab2, text="Выбрать", command=choose_color)
    btn3.grid(row=2, column=3, padx=10, pady=20)

    # вкладка "Дополнительно"
    tab3 = ttk.Frame(tab_control)
    tab_control.add(tab3, text=' Дополнительно ')
    tab_control.pack(expand=1, fill='both')
    lbFrD1 = tk.LabelFrame(tab3, width=300, height=50,text='Вид текста')
    lbFrD1.pack(fill=BOTH, padx=5, pady=10)
    lbFrD2 = tk.LabelFrame(tab3, width=300, height=50,text='Начертание текста')
    lbFrD2.pack(fill=BOTH, padx=5, pady=10)

    r_var = tk.IntVar()
    r_var.set(0)    # по радиокнопкам и чекбоксам хороший материал https://younglinux.info/tkinter/variable
    rad1 = tk.Radiobutton(lbFrD1,text='Обычный текст', variable=r_var, value=0).grid(row=1, column=0, pady=10)
    rad2 = tk.Radiobutton(lbFrD1,text='Все строчные', variable=r_var, value=1).grid(row=1, column=1, pady=10)
    rad3 = tk.Radiobutton(lbFrD1,text='Все заглавные', variable=r_var, value=2).grid(row=1, column=2, pady=10)
    tk.Label(lbFrD1, text=" ").grid(row=2, column=0, padx=10)
    chk1 = tk.Checkbutton(lbFrD2, text='Жирный').grid(row=5, column=0, padx=10, pady=10)
    chk2 = tk.Checkbutton(lbFrD2, text='Курсив').grid(row=5, column=1, padx=10, pady=10)
    chk3 = tk.Checkbutton(lbFrD2, text='Подчеркнутый').grid(row=5, column=2, padx=10, pady=10)
    tk.Label(lbFrD2, text=" ").grid(row=6, column=0, padx=10)

#-------------------------------------------------------------------------------------------------------------------------

# ИНТЕРФЕЙС ОСНОВНОГО ОКНА И РАБОЧЕЙ ОБЛАСТИ -----------------------------------------------------------------------------
root = tk.Tk()
root.title("Редактор с калькулятором")
root['bg'] = '#fafafa'
root.geometry('800x400+100+100')
root.minsize(width=800, height=400)
root.maxsize(width=800, height=400)

root.bind('<Key>', press_key)

lbFr1 = tk.LabelFrame(root, width=500, height=350, text='Редактор', font=('Arial', 12), fg='blue')
lbFr1.grid(row=1, column=0, padx=10, pady=20)
lbFr1.grid_propagate(False)    # запрет на изменение размеров при изменении размеров содержимого
lbFr2 = tk.LabelFrame(root, width=260, height=350, text='Калькулятор', font=('Arial', 12), fg='blue')
lbFr2.grid(row=1, column=1, padx=10, pady=20)
lbFr2.grid_propagate(False)    # запрет на изменение размеров при изменении размеров содержимого
mytext = ScrolledText(lbFr1, width=60,height=20, wrap = 'word', font=('Arial', 16), fg='blue')
mytext.grid(column=0,row=0)
mytext.grid_propagate(False)    # запрет на изменение размеров при изменении размеров содержимого

insert_result_button('Вставить в текст').grid(row=6, column=0, columnspan=4, rowspan=4, sticky='wens',padx=5, pady=10)
# ------------------------------------------------------------------------------------------------------------------------
# ИНТЕРФЕЙС МЕНЮ ---------------------------------------------------------------------------------------------------------
menuBar = tk.Menu(root)
fileMenu = tk.Menu(menuBar, tearoff=0)    # tearoff отключает пунктирную линию
fileMenu.add_command(label='Новый', command=NewFile)
fileMenu.add_command(label='Открыть', command=OpenFile)
fileMenu.add_command(label='Сохранить', command=SaveFile)
fileMenu.add_command(label='Сохранить как...', command=SaveAs)

menuBar.add_cascade(label='Файл', menu=fileMenu)
menuBar.add_cascade(label='Настройки', command=winSet)
menuBar.add_cascade(label='О программе', command=About)
menuBar.add_cascade(label='Выход', command=Closing)    # закрытие приложения с вопросом о выходе
#menuBar.add_cascade(label='Exit', command=root.quit) # либо без вопроса
root.config(menu=menuBar)
#--------------------------------------------------------------------------------------------------------------------------

# ИНТЕРФЕЙС КАЛЬКУЛЯТОРА --------------------------------------------------------------------------------------------------
calc = tk.Entry(lbFr2, width=20, justify=tk.RIGHT, font=('Arial', 15))
calc.insert(0, '0')    # значение в текст. поле калькулятора по умолчанию
calc['state'] = tk.DISABLED
calc.grid(row=0, column=0, columnspan=4, sticky='we', padx=5)
make_digit_button('1').grid(row=1, column=0, sticky='wens', padx=5, pady=5)
make_digit_button('2').grid(row=1, column=1, sticky='wens', padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, sticky='wens', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, sticky='wens', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, sticky='wens', padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, sticky='wens', padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, sticky='wens', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, sticky='wens', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, sticky='wens', padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, sticky='wens', padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, sticky='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, sticky='wens', padx=5, pady=5)
make_operation_button('/').grid(row=3, column=3, sticky='wens', padx=5, pady=5)
make_operation_button('*').grid(row=4, column=3, sticky='wens', padx=5, pady=5)

make_calc_button('=').grid(row=4, column=2, sticky='wens', padx=5, pady=5)

make_clear_button('C').grid(row=4, column=1, sticky='wens', padx=5, pady=5)

# устанавливаем размер колонок и строк
root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)
root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)
#------------------------------------------------------------------------------------------------------------------------

root.mainloop()