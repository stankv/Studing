# Поиск пути в графе (обход в глубину) - функция DepthFirstSearch(VFrom, VTo).

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

class Vertex:

    def __init__(self, val):
        self.Value = val
        self.hit = False    # признак того, что вершина не была посещена
  
class SimpleGraph:
	
    def __init__(self, size):
        self.max_vertex = size    # максимальное количество вершин
        self.m_adjacency = [[0] * size for _ in range(size)] # матрица смежности, где 0 - отсутствие ребра между i-й вершиной 
        # (первое измерение) и j-й вершиной (второе измерение), а 1 - наличие ребра
        self.vertex = [None] * size    # список vertex, хранящий вершины
        
    # Метод добавления новой вершины с значением v в свободное место массива vertex
    def AddVertex(self, v):
        new_vertex = Vertex(v)
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                self.vertex[i] = new_vertex
                return True
        return False
	
    # Метод удаления вершины со всеми её рёбрами (здесь и далее v - индекс вершины в списке  vertex)
    def RemoveVertex(self, v):
        if v < self.max_vertex:    # чтобы индекс массива не оказался вне его пределов
            self.vertex[v] = None
            for i in range(self.max_vertex):
                self.RemoveEdge(v, i)
                self.RemoveEdge(i, v)
            return True
        return False
	
    # Метод проверки наличия ребра (True если есть ребро между вершинами v1 и v2)
    def IsEdge(self, v1, v2):
        if v1 < self.max_vertex and v1 < self.max_vertex:
            if self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1:
                return True
        return False
	
    # Метод добавления ребра между вершинами v1 и v2
    def AddEdge(self, v1, v2):
        if v1 < self.max_vertex and v1 < self.max_vertex:
            self.m_adjacency[v1][v2] = 1
            self.m_adjacency[v2][v1] = 1
            return True
        return False
	
    # Метод удаления ребра между вершинами v1 и v2
    def RemoveEdge(self, v1, v2):
        if v1 < self.max_vertex and v1 < self.max_vertex:
            self.m_adjacency[v1][v2] = 0
            self.m_adjacency[v2][v1] = 0
            return True
        return False

    # Метод поиска пути в графе от VFrom до VTo (возвращается список узлов или [] если пути нет)
    def DepthFirstSearch(self, VFrom, VTo):
        if VFrom >= self.max_vertex or VTo >= self.max_vertex:    # проверка корректности входных данных
            return []
        working_stack = Stack()    # создаем объект типа stack, сам стек пустой
        for vertex in self.vertex:    # все вершины графа отмечаем как непосещённые
            vertex.hit = False
        X = VFrom    # выбираем текущую вершину (это индекс верщины в массиве self.vertex)
        while True:
            self.vertex[X].hit = True    # фиксируем вершину X как посещённую
            working_stack.push(self.vertex[X])    # помещаем вершину Х в стек
            if self.m_adjacency[X][VTo] == 1:    
                working_stack.push(self.vertex[VTo])
                return working_stack
            flag = False
            for i in range(self.max_vertex):
                if i == VFrom:
                    continue
                if not self.vertex[i].hit:
                    X = i
                    flag = True
                    break
            if flag:
                continue
            working_stack.pop()
            if working_stack.size == 0:
                return []
            X = self.vertex.index(working_stack.pop())
