# Проверка строки на палиндром с использованием двусторонней очереди
class Deque:
    # Инициализация внутреннего хранилища
    def __init__(self):
        self.deque = []

    # Добавление в голову
    def addFront(self, item):
        self.deque.insert(0, item)

    # Добавление в хвост
    def addTail(self, item):
        self.deque.append(item)

    # Удаление из головы
    def removeFront(self):
        if len(self.deque) > 0:
            return self.deque.pop(0)
        return None # если очередь пуста

    # Удаление из хвоста
    def removeTail(self):
        if len(self.deque) > 0:
            return self.deque.pop()
        return None # если очередь пуста

    # Размер очереди
    def size(self):
        if len(self.deque) > 0:
            return len(self.deque)
        return 0 # размер очереди

str1 = "А роза упала на лапу Азора"    # проверяемая строка

str1 = str1.lower()    # приводим все символы к нижнему регистру
print(str1)
dq1 = Deque()
for i in range(len(str1)):    # создаем из строки очередь, удаляя все пробелы
    if str1[i] == " ":
        continue
    else:
        dq1.addTail(str1[i])

# Проверка на строки на палиндром
success = True
for i in range(dq1.size() // 2):
    if dq1.removeFront() == dq1.removeTail():
        continue
    else:
        success = False

if success:
    print("Palindrome!")
else:
    print("No palindrome!")