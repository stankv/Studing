# Итератор с конструктором. Получает на вход N (количество итерируемых элементов), и флаг.
# Если flag = False, то выдает N элементов и завершает работу, иначе бесконечно выдает 
# последовательность с самого начала.
class List2:
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