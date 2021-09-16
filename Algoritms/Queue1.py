#РЕАЛИЗАЦИЯ ОЧЕРЕДИ НА ОБЫЧНОМ ПИТОНОВСКОМ СПИСКЕ
class Queue:
    def __init__(self):
        self.queue = []

    # Метод добавления элемента в конец очереди
    def enqueue(self, item):
        self.queue.append(item)    # вставка в хвост

    # Метод получения элемента из головы очереди (с его удалением)
    def dequeue(self):
        if len(self.queue) > 0:    # выдача из головы
            return self.queue.pop(0)
        return None # если очередь пустая

    # Метод вычисления длины очереди
    def size(self):
        if len(self.queue) > 0:
            return len(self.queue)
        return 0 # размер очереди