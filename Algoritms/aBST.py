# ДЕРЕВЬЯ.
# Реализация двоичного дерева в массиве.

class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        self.tree_size = 2 ** (depth + 1) - 1   # размер массива
        self.Tree = [None] * self.tree_size     # массив ключей

    def getIndexLeftChild(self, index):
        return 2 * index + 1

    def getIndexRightChild(self, index):
        return 2 * index + 2
	
    def getIndexParent(self, index):
        return (index - 1) // 2

    # Метод поиска индекса узла дерева в массиве по его ключу
    def FindKeyIndex(self, key):
        index = 0
        while index < self.tree_size:
            if self.Tree[index] == key:
                return index
            elif self.Tree[index] is None:
                return - index
            elif self.Tree[index] > key:
                index = self.getIndexLeftChild(index)
            elif self.Tree[index] < key:
                index = self.getIndexRightChild(index)
        return None # не найден
	
    # Метод добавления ключа в массив
    def AddKey(self, key):
        index = self.FindKeyIndex(key)
        if index is not None and index <= 0:
            self.Tree[abs(index)] = key
            return abs(index)    # индекс добавленного/существующего ключа или -1 если не удалось
        return -1