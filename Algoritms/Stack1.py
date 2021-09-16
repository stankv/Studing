# РЕАЛИЗАЦИЯ СТЕКА НА ОБЫЧНОМ ПИТОНОВСКОМ СПИСКЕ
class Stack:
    def __init__(self):
        self.stack = []

    # Метод вычисления текущего размера стека
    def size(self):
        return len(self.stack)

    # Метод извлечения элемента из стека
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None    # если стек пустой

    # Метод помещения элемента в стек
    def push(self, value):
        self.stack.append(value)

    # Метод получения значения последнего элемента стека без его извлечения
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return None     # если стек пустой