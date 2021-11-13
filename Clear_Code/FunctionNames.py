# 12 улучшений имён функций/методов

# 1. Рассматриваем код решения задачи 2 "Рекурсия. Вычисление суммы цифр числа" курса "JSON, XML, парсинг, сети"
# Изменено имя функции в строке 8
# РЕКУРСИВНАЯ ФУНКЦИЯ
# Вычисление суммы цифр числа N

def Calculation_sum_of_digits(Number, sum):    # было Calculation(Number,sum)
    if Number == 0:
        return sum
    else:
        sum += (Number % 10)
        return Calculation_sum_of_digits(Number // 10, sum)

def SumOfDigitsOfNumber(N):
    starting_value = 0
    return Calculation_sum_of_digits(N, starting_value)

number = int(input("Введите число:"))
print("Сумма цифр =", SumOfDigitsOfNumber(number))

# 2. Рассматриваем код решения задачи 4 "Рекурсия. Проверка, является ли строка палиндромом" курса "JSON, XML, парсинг, сети"
# Изменено имя функции в строке 28
# ИСПОЛЬЗОВАНИЕ РЕКУРСИВНОЙ ФУНКЦИИ
# Проверка, является ли строка палиндромом
def CheckPalindrom(stroka):

    def is_palindrome(Spisok):    # было Palindrome(Spisok)
        if len(L) <= 1:    # количество букв строки может быть как четным, так и нечетным
            return True    # тогда для базового условия len(L) == 0, либо == 1
        else:
            symbol_one = L.pop(0)
            symbol_end = L.pop()
            if symbol_one == symbol_end:
                return is_palindrome(L)
            else:
                return False

    # строку "переведем" в массив символов для возможности использования функции pop(), удаляя все пробелы
    L = []
    for i in range(len(stroka)):
        if stroka[i] == " ":
            continue
        else:
            L.append(stroka[i])
    
    if is_palindrome(L):
        return True
    else:
        return False

str1 = "а роза упала на лапу азора"
if CheckPalindrom(str1):
    print("Строка является палиндромом")
else:
    print("Строка НЕ является палиндромом")

# 3. Рассматриваем код решения задачи 6 "Рекурсия. Печать элементов списка с чётными индексами" 
# курса "JSON, XML, парсинг, сети"
# Изменено имя функции в строке 63
# РЕКУРСИВНАЯ ФУНКЦИЯ
# Печать элементов списка с чётными индексами
i = 0
def сalc_even_indexes_and_print(L, i):    # было Calculation(L, i)
    if i == len(L) - 1:
        print()
        return 0
    else:
        if (i % 2) == 0:
            print(" ", L[i], end='')
        i += 1
        return сalc_even_indexes_and_print(L, i)

def PrintItemsWithEvenIndexes(Spisok):
    starting_value_i = 0
    return сalc_even_indexes_and_print(Spisok, starting_value_i)

# 4. Рассматриваем код решения задачи 8 "Рекурсия. Поиск всех файлов в заданном каталоге, 
# включая файлы, расположенные в подкаталогах произвольной вложенности" курса "JSON, XML, парсинг, сети"
# Изменено имя функции в строке 83
import os

def recursive_search_of_files(path1):    # было Solve(path1)
    A = []
    for root, dirs, files in os.walk(path1):
        # Текущий каталог в рут. перебираем файлы из списка files 
        for file in files:
            A.append(os.path.join(root,file))
        for dir in dirs:
            recursive_search_of_files(os.path.join(root,dir))
    return A

def FindFiles(path):
    A = []
    if not os.path.isdir(path):    #  проверка существования каталога
        A.append(1)
        return A
    else:
        return recursive_search_of_files(path)

my_path ="E:\PROG\Temp1"
filelist1 = FindFiles(my_path)
if filelist1 == []:
    print("Каталог пустой")
elif filelist1 == [1]:
    print("Каталог не найден")
else:
    for name in filelist1:
        print(name)

# 5. Рассматриваем код решения задачи 5.3.2 "XML-документ: Функция возвращает список всех значений 
# (по всем узлам) для конкретного тега" курса "JSON, XML, парсинг, сети"
# Изменено имя функции в строке 120
import xml.etree.ElementTree as ETree
import os.path

xml1 = ETree.parse(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../4/data/demo.xml'))
root = xml1.getroot()

def get_list_values_of_tag(tag_name, root, List_values):    # было ListValues
    for i in range(len(root)):
        if len(root[i]) == 0 and root[i].tag == tag_name:
            List_values.append(root[i].text)
            return List_values
        elif len(root[i]) > 0 and root[i].tag == tag_name:
            level_down = root[i]
            for j in range(len(level_down)):
                List_values.append(level_down[j].text)
            return List_values
        elif len(root[i]) > 0 and root[i].tag != tag_name:
            level_down = root[i]
            k = False
            for j in range(len(level_down)):
                if level_down[j].tag == tag_name:
                    List_values.append(level_down[j].text)
                    k = True
            if k:
                return List_values
    return List_values

# 6. Рассматриваем код решения задачи 5.3.3 "XML-документ: РЕКУРСИВНАЯ функция, возвращает 
# количество узлов в документе, включая дочерние, оснащённые заданным атрибутом" курса "JSON, XML, парсинг, сети"
# Изменено имя функции в строке 150
import xml.etree.ElementTree as ETree
import os.path

xml1 = ETree.parse(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../4/data/demo.xml'))
root = xml1.getroot()

def get_number_of_nodes_with_spec_attrib(attr, root, L):    # было NumberOfNodes
    for i in range(len(root)):
        if attr in root[i].attrib.keys() and len(root[i]) == 0:
            L.append(1)
        elif attr in root[i].attrib.keys() and len(root[i]) > 0:
            L.append(1)
            level2 = root[i]
            get_number_of_nodes_with_spec_attrib(attr, level2, L)
        elif not attr in root[i].attrib.keys() and len(root[i]) > 0:
            level2 = root[i]
            get_number_of_nodes_with_spec_attrib(attr, level2, L)
    return sum(L)

# 7. Рассматриваем код решения задачи 6.6.1 "XML-документ: Функция формирует список всех узлов 
# по заданному тегу в XML-документе. На вход функция получает корневой узел и тег" 
# курса "JSON, XML, парсинг, сети".
# Изменено имя функции в строке 173
import xml.etree.ElementTree as ETree
import os.path

xml1 = ETree.parse(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../4/data/demo.xml'))
root = xml1.getroot()

def get_list_all_nodes_of_tag(root_node, tag_name):    # было ListOfNodes
    List_values =[]
    # ищем в документе теги с заданным именем
    for item in root_node.iter():
        if item.tag != tag_name:
            continue
        elif item.tag == tag_name and len(item) == 0:     # тег не имеет дочерних тегов
            List_values.append(item.tag)
        elif item.tag == tag_name and len(item) > 0:    # тег имеет дочерние теги
            for subitem in item.iter():
                List_values.append(subitem.tag)
    return List_values

# 8. Рассматриваем код решения задачи 6.6.2 "XML-документ: Функция находит родителя заданного (по имени тега) узла, 
# и возвращает его (тип Element)" курса "JSON, XML, парсинг, сети".
# Изменено имя функции в строке 195
import xml.etree.ElementTree as ETree
import os.path

xml1 = ETree.parse(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../4/data/demo.xml'))
root = xml1.getroot()

def get_parent_of_node(root_node, tag_name):    # рекурсивная функция! было ParentOfNode
    if root_node.find(tag_name) != None:
        return root_node
    else:
        for item in root_node:
            if len(item) > 0:
                if item.find(tag_name) != None:
                    return item
                else:
                    get_parent_of_node(item, tag_name)

# 9. Рассматриваем код решения задачи 6.6.3 "XML-документ: Функция удаляет все узлы 
# по заданному тегу в XML-документе" курса "JSON, XML, парсинг, сети".
# Изменено имя функции в строке 216
import xml.etree.ElementTree as ETree
import os.path

my_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../4/data/demo.xml')
xml1 = ETree.parse(my_path)
root = xml1.getroot()

def delete_all_nodes_on_given_tag(root_node, tag_name, path):    # было DelOfNodes
    success = False
    for item in root_node.iter():    # Идем по всем узлам документа
        if item.find(tag_name) != None:    # Если тег найден, то удаляем его
            for lng in item.findall(tag_name):
                item.remove(lng)
            success = True
    if success:    # Если тег был найден и удален, то перезаписываем файл
        serialze = ETree.tostring(root_node, encoding='utf8', method='xml').decode()
        fil = open(path, "w")  
        fil.write(serialze)

# 10 и 11. Рассматриваем код решения задачи "Одновременные процессы: функция, которая получает на вход 
# большой список вещественных чисел, и количество процессов, которое должно просуммировать этот массив 
# по кусочкам" курса "JSON, XML, парсинг, сети".
# Изменено имя функции в строке 236, 237
import random
import time
from threading import Thread

def Concurrency_summation_of_items_of_array(N, L):    # было Concurrency(N, L)
    def сalc_sum_items_of_subarray(id, Spisok, res):    # было Calculate
        sum = 0
        for ani in Spisok:
            sum += ani
            time.sleep(0.05)
        res[id] = sum

    # Разбиваем массив L на N частей, создаем 2-мерный массив из этих частей
    k = len(L) // N
    if k == 0:    # число операций в каждом потоке должно быть не меньше 1
        return sum(L)
    N1 = 0
    N2 = k
    S = []
    for i in range(N):
        b = []
        for j in L[N1:N2]:
            b.append(j)
        S.append(b)
        if i < N - 2:
            N1 += k
            N2 += k
        elif i == N - 2:
            N1 += k
            N2 = len(L)

    # Запускаем N процессов счета (N функций Calculate)
    results = {}    # результаты работы процессов запишем в словарь
    Threads = []
    i = 1    # - id процесса
    for submassiv in S:
        t = Thread(target=сalc_sum_items_of_subarray, name="Thread", args=(i,submassiv,results))
        Threads.append(t)
        t.start()
        i += 1
    # ожидаем окончания выполнения всех процессов
    proc_running = True
    while(proc_running):
        proc_running = False
        for t in Threads:
            if t.is_alive():
                proc_running = True
                break    # сразу выходим из for если данный процесс продолжается
    success = sum(results.values())    # суммируем результаты работы процессов
    return success

# 12. Рассматриваем код решения задачи "КОНСОЛЬНЫЙ TCP-ЧАТ-СЕРВЕР" курса "JSON, XML, парсинг, сети".
# Изменено имя функции в строке 289
import socket
import threading

# Функция отправки сообщений всем клиентам
def send_all_users(message, current_client):    # было broadcast
    for client in clients:    # отправляем всем, кроме того, кто прислал
        if client == current_client:
            continue
        client.send(message)

# Функция обработки сообщений от клиентов
def handle(client):
    while True:
        try:
            # Отправка сообщения клиентам
            message = client.recv(1024)    # получаем сообщение от клиента
            send_all_users(message, client)    # рассылаем его всем другим клиентам
            print(message.decode('utf-8'))
        except:
            # Если ошибка, удаляем из списков объект типа сокет клиента и его ник
            index = clients.index(client)
            clients.remove(client)
            client.close()    # закрываем объект типа сокет клиента
            nickname = nicknames[index]
            send_all_users('{} is disconnect!'.format(nickname).encode('utf-8'), None)
            print(nickname, "is disconnect")
            nicknames.remove(nickname)
            break

# Основная функция программы. Прослушивание порта, подключение новых клиентов
def receive():
    while True:
        # Принимаем подключение клиента
        client, address = server.accept()    # ожидаем и принимаем соединение с клиентом
        print("Connected with {}".format(str(address)))

        # Запрашиваем имя/ник клиента, сохраняем данные клиента в списках
        client.send('NICK'.encode('utf-8'))    # отправляем клиенту запрос его имени/ника
        nickname = client.recv(1024).decode('utf-8')    # ожидаем и получаем ответ клиента
        nicknames.append(nickname)
        clients.append(client)

        # Сообщаем о подключении нового клиента
        print("Nickname is {}".format(nickname))
        send_all_users("{} joined!".format(nickname).encode('utf-8'), None)
        client.send('Connected to server!'.encode('utf-8'))

        # Запуск отдельного потока приема/отправки сообщений для подключившегося клиента
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

# функция запуска отключения сервера
def server_off():
    while True:
        comm = input()
        if comm == 'bye':
            if len(clients) != 0:    # если есть подключенные клиенты, то закрываем соединения
                send_all_users('Server shutdown!'.encode('utf-8'), None)
                for client in clients:
                    client.close()
            #server.shutdown(socket.SHUT_RDWR)
            server.close()
            print("Server Deactivated!")
            break

# Данные для подключения к серверу
host = 'localhost'
port = 12345

# Запуск сервера
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # создаем TCP-сокет
server.bind((host, port))    # привязываем сокет к адресу и порту
server.listen()    # перевод сокета в режим сервера и прослушивания порта
print("Server Activated!")

# Списки объектов типа сокет подключенных клиентов и ников клиентов
clients = []
nicknames = []
# Запуск потока для функции отключения сервера
thread_off = threading.Thread(target=server_off)
thread_off.start()
receive()