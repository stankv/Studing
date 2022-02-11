# Уязвимые графы.
# Поиск узлов, не входящих ни в один треугольник в графе - функция WeakVertices().
# Некоторая вершина графа считается принадлежащей треугольнику, если среди её прямых вершин-соседей 
# (с которыми она связана рёбрами) имеются хотя бы две вершины, связанные ребром друг с другом. 

class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False    # признак того, что вершина не была посещена
  
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
        if v1 < self.max_vertex and v2 < self.max_vertex:
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

    # Метод поиска узлов, не входящих ни в один треугольник
    def WeakVertices(self):
        if len(self.vertex) == 0:
            return []
        elif len(self.vertex) <= 2:
            return self.vertex

        working_list = []
        for i in range(self.max_vertex):
            list_adjacent_vertices = []
            for j in range(self.max_vertex):
                if self.IsEdge(i, j):
                    list_adjacent_vertices.append(j)
        
            n = len(list_adjacent_vertices)
            if n == 0:
                continue
            elif n == 1:
                if self.IsEdge(list_adjacent_vertices[0], list_adjacent_vertices[0]):
                    working_list.append(i)
                    working_list.append(list_adjacent_vertices[0])
            elif n > 1:
                for j in range(n):
                    for k in range(j + 1, n):
                        if self.IsEdge(list_adjacent_vertices[j], list_adjacent_vertices[k]):
                            working_list.append(i)
                            working_list.append(list_adjacent_vertices[j])
                            working_list.append(list_adjacent_vertices[k])

        list_indexes_all_vertex = [i for i in range(self.max_vertex)]
        working_list = list(set(list_indexes_all_vertex) - set(working_list))
        if working_list == []:
            return []
        result = []
        for i in working_list:
            result.append(self.vertex[i])
        return result

"""z = SimpleGraph(6)
z.AddVertex('A')
z.AddVertex('B')
z.AddVertex('C')
z.AddVertex('D')
z.AddVertex('E')
z.AddVertex('F')
for i in z.vertex:
    print(i.Value)
#z.m_adjacency = [[0,1,1,1,0,0], [1,0,0,1,1,0], [1,0,0,1,0,0], [1,1,1,1,1,0], [0,1,0,1,0,0], [0,0,0,0,0,0]]
#z.m_adjacency = [[0,1,1,0,0,0], [1,0,0,1,1,0], [1,0,0,1,0,0], [0,1,1,0,1,0], [0,1,0,1,0,0], [0,0,0,0,0,0]]
z.m_adjacency = [[0,1,1,1,0,0], [1,0,0,1,1,0], [1,0,0,1,0,0], [1,1,1,1,0,0], [0,1,0,0,0,0], [0,0,0,0,0,0]]
res = z.WeakVertices()
print(res)
for i in res:
    print(i.Value)"""