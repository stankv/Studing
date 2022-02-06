# ГРАФЫ.
# Реализация простого графа.

class Vertex:

    def __init__(self, val):
        self.Value = val
  
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