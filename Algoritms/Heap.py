# Реализация пирамиды (кучи). Корень - максимальный элемент).

class Heap:

    def __init__(self):
        self.HeapArray = [] # хранит неотрицательные числа-ключи
    
    def getIndexLeftChild(self, index):
        return 2 * index + 1

    def getIndexRightChild(self, index):
        return 2 * index + 2
	
    def getIndexParent(self, index):
        return (index - 1) // 2
		
    # создаём массив кучи HeapArray из заданного, размер массива выбираем на основе глубины depth 
    def MakeHeap(self, a, depth):
        self.Size = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * self.Size
        for key in a:
            self.Add(key)

    # возвращает значение корня и перестраивает кучу
    def GetMax(self):
        if self.HeapArray == [] or self.HeapArray[0] is None:
	        return -1 # если куча пуста
        if self.Size == 1:
            max_key = self.HeapArray[0]
            self.HeapArray[0] = None
            return max_key
        elif self.HeapArray[0] is not None and (self.HeapArray[1] is None and self.HeapArray[2] is None):
            max_key = self.HeapArray[0]
            self.HeapArray[0] = None
            return max_key
        elif self.HeapArray[0] is not None and (self.HeapArray[1] is None or self.HeapArray[2] is None):
            if self.HeapArray[1] is not None:
                max_key = self.HeapArray[0]
                self.HeapArray[0] = self.HeapArray[1]
                self.HeapArray[1] = None
                return max_key
            elif self.HeapArray[2] is not None:
                max_key = self.HeapArray[0]
                self.HeapArray[0] = self.HeapArray[2]
                self.HeapArray[2] = None
                return max_key

        if self.HeapArray[-1] is not None:
            index = -1
        else:
            for index in range(1, len(self.HeapArray)):
                if self.HeapArray[index] == None and self.HeapArray[index - 1] != None:
                    index = index - 1
                    break
        max_key = self.HeapArray[0]
        self.HeapArray[0] = self.HeapArray[index]
        self.HeapArray[index] = None

        index = 0
        while True:
            index_leftchild = self.getIndexLeftChild(index)
            index_rightchild = self.getIndexRightChild(index)
            if index_leftchild >= self.Size or index_rightchild >= self.Size:
                return max_key
            if self.HeapArray[index_leftchild] is None and self.HeapArray[index_rightchild] is None:
                return max_key
            elif self.HeapArray[index_leftchild] is not None and self.HeapArray[index_rightchild] is None:
                if self.HeapArray[index] < self.HeapArray[index_leftchild]:
                    self.HeapArray[index], self.HeapArray[index_leftchild] = self.HeapArray[index_leftchild], self.HeapArray[index]
                    index = index_leftchild
                else:
                    return max_key
            elif self.HeapArray[index_leftchild] is None and self.HeapArray[index_rightchild] is not None:
                if self.HeapArray[index] < self.HeapArray[index_rightchild]:
                    self.HeapArray[index], self.HeapArray[index_rightchild] = self.HeapArray[index_rightchild], self.HeapArray[index]
                    index = index_rightchild
                else:
                    return max_key
            elif self.HeapArray[index_leftchild] is not None and self.HeapArray[index_rightchild] is not None:
                if self.HeapArray[index] >= self.HeapArray[index_leftchild] and self.HeapArray[index] >= self.HeapArray[index_rightchild]:
                    return max_key
                elif self.HeapArray[index] >= self.HeapArray[index_leftchild] and self.HeapArray[index] < self.HeapArray[index_rightchild]:
                    self.HeapArray[index], self.HeapArray[index_rightchild] = self.HeapArray[index_rightchild], self.HeapArray[index]
                    index = index_rightchild
                elif self.HeapArray[index] < self.HeapArray[index_leftchild] and self.HeapArray[index] >= self.HeapArray[index_rightchild]:
                    self.HeapArray[index], self.HeapArray[index_leftchild] = self.HeapArray[index_leftchild], self.HeapArray[index]
                    index = index_leftchild
                elif self.HeapArray[index] < self.HeapArray[index_leftchild] and self.HeapArray[index] < self.HeapArray[index_rightchild]:
                    if self.HeapArray[index_leftchild] < self.HeapArray[index_rightchild]:
                        self.HeapArray[index], self.HeapArray[index_rightchild] = self.HeapArray[index_rightchild], self.HeapArray[index]
                        index = index_rightchild
                    elif self.HeapArray[index_leftchild] > self.HeapArray[index_rightchild]:
                        self.HeapArray[index], self.HeapArray[index_leftchild] = self.HeapArray[index_leftchild], self.HeapArray[index]
                        index = index_leftchild
                    # вариант, когда оба потомка равны друг другу здесь не был предусмотрен.


    # добавляем новый элемент key в кучу и перестраиваем её
    def Add(self, key):
        if self.HeapArray == []:
            return False
        if self.HeapArray[-1] is not None:
	        return False # если куча вся заполнена
        if self.HeapArray[0] == None:
            self.HeapArray[0] = key
            return True
        for index in range(1, len(self.HeapArray)):
            if self.HeapArray[index] == None and self.HeapArray[index - 1] != None:
                self.HeapArray[index] = key
                break
        while True:
            index_parent = self.getIndexParent(index)
            if self.HeapArray[index] < self.HeapArray[index_parent]:
                return True
            elif self.HeapArray[index] > self.HeapArray[index_parent]:
                self.HeapArray[index], self.HeapArray[index_parent] = self.HeapArray[index_parent], self.HeapArray[index]
                if index_parent == 0:
                    return True
                index = index_parent

"""My_Heap = Heap()
My_Heap.MakeHeap([8,5,3,2],2)
print(My_Heap.HeapArray)
print(My_Heap.GetMax())
print(My_Heap.HeapArray)
print(My_Heap.GetMax())
print(My_Heap.HeapArray)
print(My_Heap.GetMax())
print(My_Heap.HeapArray)
print(My_Heap.GetMax())
print(My_Heap.HeapArray)"""