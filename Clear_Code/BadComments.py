# Плохие комментарии
# Найдите 15 своих плохих комментариев, и напишите по каждому, что вы сделали для их улучшения с указанием 
# соответствующего пункта из занятия. 

# 1-5. Рассматриваем код решения задачи "Безумный Макс" курса "28 задач".
# Строки 11, 14, 16 и 19 - шум. Комментарии удаляются.
# Строка 22 - бормотание. Меняем на "с середины массива Tele сортируем его элементы по убыванию"
def MadMax(N, Tele):
    is_not_sorted = True
    while(is_not_sorted):
        is_not_sorted = False     # предполагаем, что массив уже отсортирован
        for i in range(N - 1):
            if Tele[i] > Tele[i+1]:
            # нашли элементы,неупорядоченные по возрастанию, меняем их местами:
                Tele[i], Tele[i+1] = Tele[i+1], Tele[i]
            # цикл проверки массива надо продожить снова:
                is_not_sorted = True
                
    # меняем местами срединный элемент и последний (наибольший)
    Tele[N // 2 ], Tele[N - 1] = Tele[N - 1], Tele[N // 2]
   
    # с середины сортируем элементы по убыванию   
    is_not_sorted = True
    while(is_not_sorted):
        is_not_sorted = False
        for i in range((N // 2) + 1, N - 1):
            if Tele[i] < Tele[i+1]:
                Tele[i + 1], Tele[i] = Tele[i], Tele[i + 1]
                is_not_sorted = True
    return Tele

# 6-8. Рассматриваем код решения задачи "Восстановление таблицы зарплат" курса "28 задач"
# Строки 38 и  50 - шум (удаляем комментарии)
# Строка 65 - комментарий, где можно использовать функцию или переменную. Комментарий удаляем, 
# имя переменной k меняем на employee_id (или employee_number)
def SynchronizingTables(N, ids, salary):
    
    # делаем копии массивов для дальнейшей работы
    ids_copy = []
    for i in range(N):
        ids_copy.append(ids[i])
    
    salary_copy = []
    for i in range(N):
        salary_copy.append(salary[i])
    
    # сортируем оба списка по возрастанию
    is_not_sorted = True
    while(is_not_sorted):
        is_not_sorted = False # предполагаем, что массив уже отсортирован
        for i in range(N - 1):
            if ids_copy[i] > ids_copy[i+1]:
                ids_copy[i], ids_copy[i+1] = ids_copy[i+1], ids_copy[i]
                is_not_sorted = True

    is_not_sorted = True 
    while(is_not_sorted):
        is_not_sorted = False
        for i in range(N - 1):
            if salary_copy[i] > salary_copy[i+1]:
                salary_copy[i], salary_copy[i+1] = salary_copy[i+1], salary_copy[i]
                is_not_sorted = True
 
    for i in range(N):
        k = ids[i]    # читаем номер сотрудника
        # ищем в отсортированном массиве этот номер и получаем номер элемента
        for j in range(N):
            if ids_copy[j] == k:
                salary[i] = salary_copy[j]
                break
    return salary

# 9-10. Рассматриваем код решения задачи "Искусственный интеллект для Оксаны" курса "28 задач".
# Строки 76 и 81 - шум. Комментарии удаляются.
def SumOfThe(N, data):
    # считаем сумму всего массива
    full_sum = 0
    for i in range(N):
        full_sum = full_sum + data[i]

    # ищем число, равное сумме всех элементов массива без него
    result = 0
    for i in range(N):
        if (full_sum - data[i]) == data[i]:
            result = data[i]
            break
    return result

# 11. Рассматриваем код решения задачи "Чат-сервер" курса "JSON, XML, парсинг, сети"
# https://github.com/stankv/Studing/blob/main/4/TCPchat_server.py
# Рассмотрим функцию отключения сервера:
def server_off():
    while True:
        comm = input()
        if comm == 'bye':
            if len(clients) != 0:    # если есть подключенные клиенты, то закрываем соединения
                broadcast('Server shutdown!'.encode('utf-8'), None)
                for client in clients:
                    client.close()
            #server.shutdown(socket.SHUT_RDWR)
            server.close()
            print("Server Deactivated!")
            break
# Строка 100 - закомментированный (не используемый код). Комментарий удаляется.

# 12-13. Рассматриваем код решения задачи "Однонаправленный связанный список" курса "Алгоритмы и структуры данных 1"
# https://github.com/stankv/Studing/blob/main/Algoritms/LinkedList1.py
# Строка 114 - комментарий, где можно использовать функцию или переменную. Комментарий удаляем, 
# имя переменной k меняем на length_LinkedList
# Строка 116 - шум. Комментарий удаляем.

# много кода......
def delete(self, val, all=False):
        k = self.len()    # вычисляем длину списка 1 раз, чтобы не делать этого каждый раз дальше
        node = self.head
        if k == 0:    # если список пустой то ничего не делаем
            return
        # много кода....

# 14-16. Рассматриваем код решения задачи "Двунаправленный связанный список" курса "Алгоритмы и структуры данных 1"
# https://github.com/stankv/Studing/blob/main/Algoritms/LinkedList2.py
# Строка 127 - избыточный комментарий. Удаляем .
# Строка 129 - шум (очевидный комментарий). Комментарий удаляем.
# Строка 130 - закомментированный (ненужный) код. Комментарий (строку) удаляем.

# много кода....
# 7. Метод вставки узла самым первым элементом
    def add_in_head(self, newNode):
        if self.head is None:    # если список пустой
            #self.head = newNode    # неверно, этого не достаточно
            self.add_in_tail(newNode)
            return
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        return
    # много кода....
