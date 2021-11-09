# Имена классов. Улучшение 5 имен классов.

# 1. Рассматриваем код решения задачи "Итераторы" курса "JSON, XML, парсинг, сети"
# Изменены имена классов в строках: 6
# Итератор с конструктором
class Simple_Iterator_Doubling_Numbers:    # было List2
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self): 
        current = self.start
        self.start = self.start * 2
        self.count += 1
        if self.count <= 10:
            return current
        raise StopIteration

# 2. Рассматриваем код решения задачи "Итераторы" курса "JSON, XML, парсинг, сети"
# Изменены имена классов в строках: 24
class Circular_Iterator_Doubling_Numbers:    # было List2
    def __init__(self, N, flag):
        self.N = N
        self.flag = flag

    def __iter__(self):
        self.start = 1
        self.count = 0
        return self

    def __next__(self): 
        if self.flag:    # flag = True - бесконечность
            current = self.start
            self.start = self.start * 2
            self.count += 1
            if self.count <= self.N:
                return current
            else:
                self.start = 1
                self.count = 1
                current = self.start
                self.start = 2
                return current
        else:
            current = self.start
            self.start = self.start * 2
            self.count += 1
            if self.count <= self.N:
                return current
            raise StopIteration

# 3. Рассматриваем код решения задач курса "Алгоритмы и структуры данных - 1"
# Однонаправленный список - https://github.com/stankv/Studing/blob/main/Algoritms/LinkedList1.py
# имя класса LinkedList -> SimpleLinkedList

# 4. Рассматриваем код решения задач курса "Алгоритмы и структуры данных - 1"
# Двунаправленный список - https://github.com/stankv/Studing/blob/main/Algoritms/LinkedList2.py
# имя класса LinkedList2 -> DoubleLinkedList

# 5. Рассматриваем код решения задач курса "Алгоритмы и структуры данных - 1"
# Двунаправленная очередь - https://github.com/stankv/Studing/blob/main/Algoritms/Deque1.py
# имя класса Deque -> DoubleQueue

# -------------------------------------------------------------------------------------------------------------------------

# Улучшение имен 7 методов и объектов
# Приводим все имена методов в задачах курса "Алгоритмы и структуры данных - 1" к одному виду, т.е. в именах методов 
# используем только: add(item), pop(), add_in_head, add_in_tail, insert(item), get() или get(item) и т.д.
# 1. Однонаправленная очередь - https://github.com/stankv/Studing/blob/main/Algoritms/Queue1.py
# метод добавления элемента в очередь: enqueue(item) -> append(item)

# 2. Однонаправленная очередь - https://github.com/stankv/Studing/blob/main/Algoritms/Queue1.py
# метод извлечения элемента из головы очереди: dequeue() -> pop()

# 3. Двунаправленная очередь - https://github.com/stankv/Studing/blob/main/Algoritms/Deque1.py
# добавление элемента в голову: addFront(item) -> add_in_head(item)

# 4. Двунаправленная очередь - https://github.com/stankv/Studing/blob/main/Algoritms/Deque1.py
# добавление элемента в хвост: addTail(item) -> add_in_tail(item)

# 5. Двунаправленная очередь - https://github.com/stankv/Studing/blob/main/Algoritms/Deque1.py
# удаление элемента из головы: removeFront() -> delete_head()

# 6. Двунаправленная очередь - https://github.com/stankv/Studing/blob/main/Algoritms/Deque1.py
# удаление элемента из хвоста: removeTail() -> delete_tail()

# 7. Стек - https://github.com/stankv/Studing/blob/main/Algoritms/Stack1.py
# метод помещения элемента в стек: push(value) -> add(value)

# 8. Стек - https://github.com/stankv/Studing/blob/main/Algoritms/Stack1.py
# метод получения значения последнего элемента без его извлечения: peek() -> get()
