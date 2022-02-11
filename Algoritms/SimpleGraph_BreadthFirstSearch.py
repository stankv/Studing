# Поиск пути в графе (обход в ширину) - функция BredthFirstSearch(VFrom, VTo).

# Односторонняя очередь
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

    # Метод поиска пути в графе в ширину (кратчайший путь), от VFrom до VTo (возвращается список узлов или [] если пути нет)
    def BreadthFirstSearch(self, VFrom, VTo):    # VFrom и VTo индексы массива self.vertex
        def MakePath(dictionary, vfrom, vto):
            list_indexes = []
            x = vto
            while x != vfrom:
                for key in dictionary.keys():
                    if x in dictionary[key]:
                        list_indexes.append(x)
                        x = key
            list_indexes.append(vfrom)
            list_indexes = list(reversed(list_indexes))
            result = []
            for index in list_indexes:
                result.append(self.vertex[index])
            return result

        if VFrom >= self.max_vertex or VTo >= self.max_vertex:
            return []
        if VFrom == VTo:
            if self.IsEdge(VFrom, VTo):
                return [self.vertex[VFrom], self.vertex[VTo]]
            return []

        working_queue = Queue()  # делаем очередь пустой
        for vertex in self.vertex: # все вершины графа отмечаем как непосещённые
            vertex.Hit = False
        X = VFrom # Выбираем текущую вершину
        self.vertex[X].Hit = True # фиксируем вершину как посещённую.
        working_dict = {}
        while True:
            working_dict[X] = []
            for i in range(self.max_vertex):
                if self.IsEdge(X, i) and self.vertex[i].Hit is False: # добавляем в очередь все смежные непосещ вершины
                    working_dict[X].append(i)
                    if i == VTo:
                        return MakePath(working_dict, VFrom, VTo)# возвращаем путь
                    self.vertex[i].Hit = True # фиксируем вершину как посещённую.
                    working_queue.enqueue(i)  # добавляем ее в очередь
            if working_queue.size == 0: # если очередь пуста
                return []
            X = working_queue.dequeue()
        

"""z = SimpleGraph(6)
z.AddVertex('A')
z.AddVertex('B')
z.AddVertex('C')
z.AddVertex('D')
z.AddVertex('E')
z.AddVertex('F')
for i in z.vertex:
    print(i.Value)
print()
z.m_adjacency = [[0,1,0,0,0,0], [1,0,1,1,0,0], [0,1,0,1,0,0], [0,1,1,1,1,0], [0,0,0,1,0,0], [0,0,0,0,0,0]]
#z.m_adjacency = [[0,1,1,1,0,0], [1,0,0,1,1,0], [1,0,0,1,0,0], [1,1,1,1,1,0], [0,1,0,1,0,0], [0,0,0,0,0,0]]
res = z.BreadthFirstSearch(4, 0)
print(res)
for i in res:
    print(i.Value)"""
