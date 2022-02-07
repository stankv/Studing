class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val    # значение в узле
        self.Parent = parent    # родитель или None для корня
        self.Children = []      # список дочерних узлов
	
class SimpleTree:
    def __init__(self, root):
        self.Root = root # корень, может быть None
	
    # Метод добавления нового дочернего узла к существующему ParentNode
    def AddChild(self, ParentNode, NewChild):
        if self.Root is None:
            self.Root = NewChild
        elif self.Root is not None and ParentNode is None:
            pass
        else:
            NewChild.Parent = ParentNode
            ParentNode.Children.append(NewChild)
  
    # Метод удаления существующего некорневого узла NodeToDelete
    def DeleteNode(self, NodeToDelete):
        if NodeToDelete is self.Root and self.Root.Children == []:
            self.Root = None
        elif NodeToDelete is self.Root and self.Root.Children != []:
            pass
        else:
            NodeToDelete.Children.clear()
            NodeToDelete.Parent.Children.remove(NodeToDelete)
            NodeToDelete.Parent = None
            NodeToDelete = None
    
    # Метод выдачи всех узлов дерева в определённом порядке
    def GetAllNodes(self):
        # рекурсивный обход дерева в глубину
        def Count_Nodes(Node, list_all_nodes, visited_nodes):
            if Node.Children != []:
                list_all_nodes.extend(Node.Children)
            for Children in Node.Children:
                if Children not in visited_nodes:
                    visited_nodes.append(Children)
                    Count_Nodes(Children, list_all_nodes, visited_nodes)
            return list_all_nodes
        
        if self.Root is None:
            return []
        elif self.Root is not None and self.Root.Children == []:
            return [self.Root]
        else:
            return Count_Nodes(self.Root, [self.Root], [self.Root])
    
    # Метод поиска узлов по значению
    def FindNodesByValue(self, val):
        # рекурсивный обход дерева
        def Count_Nodes(node, list_all_nodes):
            if node.Children == []:
                return list_all_nodes
            else:
                list_all_nodes.extend(node.Children)
                for Child in node.Children:
                    Count_Nodes(Child, list_all_nodes)
            return list_all_nodes

        if self.Root is not None:
            list_all_nodes = Count_Nodes(self.Root, [self.Root])
            nodes_by_value = []
            for node in list_all_nodes:
                if node.NodeValue == val:
                    nodes_by_value.append(node)
            return nodes_by_value
        else:
            return []
   
    # Метод перемещения узла вместе с его поддеревом в качестве дочернего для узла NewParent
    def MoveNode(self, OriginalNode, NewParent):
        OriginalNode.Parent.Children.remove(OriginalNode)
        OriginalNode.Parent = NewParent
        NewParent.Children.append(OriginalNode)
   
    # Метод получения количества всех узлов в дереве
    def Count(self):
        if self.Root is not None:
            return len(self.GetAllNodes())
        else:
            return 0

    # Метод получения списка листьев дерева
    def GetAllLeafs(self):
        if self.Root is None:
            return []
        elif self.Root is not None and self.Root.Children == []:
            return [self.Root]
        else:
            list_all_nodes = self.GetAllNodes()
            leafs = []
            for Node in list_all_nodes:
                if Node.Children == []:
                    leafs.append(Node)
            return leafs

    # Метод получения количества листьев в дереве
    def LeafCount(self):
        if self.Root is None:
            return 0
        elif self.Root is not None and self.Root.Children == []:
            return 1
        list_all_nodes = self.GetAllNodes()
        leafs = []
        for Node in list_all_nodes:
            if Node.Children == []:
                leafs.append(Node)
        return len(leafs)
    
    # Метод, который перебирает всё дерево и прописывает каждому узлу его уровень.
    def GetAllNodesWithLevel(self):
        def Level_Of_Each_Node(node, dict_all_nodes, level_nodes):
            if node.Children == []:
                return dict_all_nodes
            else:
                level_nodes += 1
                for Child in node.Children:
                    dict_all_nodes[Child] = level_nodes
                    Level_Of_Each_Node(Child, dict_all_nodes, level_nodes)
            return dict_all_nodes

        if self.Root is not None:
            return Level_Of_Each_Node(self.Root, {self.Root:0}, 0)
        return None

    # Метод получения пар узлов, между которыми нужно разорвать связь для получения леса четных деревьев
    def EvenTrees(self):

        def GetListNodesSubtree(Node, list_nodes_subtree, visited_nodes):    # получаем список узлов поддерева
            if Node.Children != []:
                list_nodes_subtree.extend(Node.Children)
            for Children in Node.Children:
                if Children not in visited_nodes:
                    visited_nodes.append(Children)
                    GetListNodesSubtree(Children, list_nodes_subtree, visited_nodes)
            return list_nodes_subtree

        def CountNodesSubtree(node):    # получаем число узлов поддерева
            if node is None:
                return 0
            elif node is not None and node.Children == []:
                return 1
            else:
                return len(GetListNodesSubtree(node, [node], [node]))

        if self.Count() % 2 != 0:
            return []
        list_leaves = self.GetAllLeafs()
        list_connections = []
        for i in range(len(list_leaves)):
            node = list_leaves[i]
            while node.Parent != self.Root:
                if CountNodesSubtree(node.Parent) % 2 == 0 and node.Parent not in list_connections:
                    list_connections.append(node.Parent.Parent)
                    list_connections.append(node.Parent)
                node = node.Parent
        return list_connections