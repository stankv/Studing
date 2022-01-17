# ДЕРЕВЬЯ
# Реализация простого дерева (общий случай) и его методов.

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
        # рекурсивный обход дерева
        def Count_Nodes(node, list_all_nodes):
            if node.Children == []:
                return list_all_nodes
            else:
                list_all_nodes.extend(node.Children)
                for Child in node.Children:
                    Count_Nodes(Child, list_all_nodes)
            return list_all_nodes
        
        if self.Root is None:
            return []
        elif self.Root is not None and self.Root.Children == []:
            return [self.Root]
        else:
            return Count_Nodes(self.Root, [self.Root])
    
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

    # Метод получения количества листьев в дереве
    def LeafCount(self):
        # рекурсивный обход дерева
        def Count_Leaves(node, list_all_nodes, leaves):
            if node.Children == []:
                leaves.append(0)
                return list_all_nodes
            else:
                list_all_nodes.extend(node.Children)
                for Child in node.Children:
                    Count_Leaves(Child, list_all_nodes, leaves)
            return len(leaves)
        
        if self.Root is None:
            return 0
        elif self.Root is not None and self.Root.Children == []:
            return 1
        else:
            return Count_Leaves(self.Root, [self.Root], [])
    

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

"""node0 = SimpleTreeNode(9, None)
node1 = SimpleTreeNode(4, None)
node2 = SimpleTreeNode(17, None)
node3 = SimpleTreeNode(3, None)
node4 = SimpleTreeNode(6, None)
node5 = SimpleTreeNode(22, None)
node6 = SimpleTreeNode(5, None)
node7 = SimpleTreeNode(7, None)
node8 = SimpleTreeNode(20, None)
node9 = SimpleTreeNode(10, None)
node10 = SimpleTreeNode(11, None)
node11 = SimpleTreeNode(12, None)
node12 = SimpleTreeNode(13, None)
node13 = SimpleTreeNode(14, None)
node14 = SimpleTreeNode(11, None)

My_Tree = SimpleTree(node0)
My_Tree.AddChild(node0, node1)
My_Tree.AddChild(node0, node2)
My_Tree.AddChild(node1, node3)
My_Tree.AddChild(node1, node4)
My_Tree.AddChild(node4, node6)
My_Tree.AddChild(node4, node7)
My_Tree.AddChild(node2, node5)
My_Tree.AddChild(node5, node8)
My_Tree.AddChild(node0, node9)
My_Tree.AddChild(node9, node10)
My_Tree.AddChild(node9, node11)
My_Tree.AddChild(node11, node12)
My_Tree.AddChild(node11, node13)
My_Tree.AddChild(node11, node14)

print(node1.NodeValue)
for i in node1.Children:
    print(i.NodeValue, ' ', end='')
print()
print()
AllNodes = My_Tree.GetAllNodes()
print(AllNodes)
for i in AllNodes:
    print(i.NodeValue)
print()
print()
print(My_Tree.Count())
print()
print(My_Tree.LeafCount())
print()
print(My_Tree.FindNodesByValue(11))
print()
dict_nodes = My_Tree.GetAllNodesWithLevel()
for i in dict_nodes:
    print(i.NodeValue, " ", dict_nodes[i])"""