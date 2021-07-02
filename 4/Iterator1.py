# Итератор с конструктором
class List2:
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