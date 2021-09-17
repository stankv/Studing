#РЕАЛИЗАЦИЯ ДВУСТОРОННЕЙ ОЧЕРЕДИ НА ОБЫЧНОМ ПИТОНОВСКОМ СПИСКЕ
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