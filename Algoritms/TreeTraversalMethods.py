# ДЕРЕВЬЯ.
# Реализация двоичного дерева поиска. Реализация методов обхода дерева.

from typing import Tuple


class BSTNode:
	
    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


class BSTFind: # промежуточный результат поиска

    def __init__(self):
        self.Node = None # None если в дереве вообще нет узлов
        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node # корень дерева, или None

    # Метод поиска узла по его ключу (возвращает объект BSTFind)
    def FindNodeByKey(self, key):

        def FindNode(Node, key):
            while True:
                if Node.NodeKey == key:
                    return Node
                elif Node.NodeKey > key:
                    if Node.LeftChild:
                        Node = Node.LeftChild
                        continue
                    else:
                        return Node
                elif Node.NodeKey < key:
                    if Node.RightChild:
                        Node = Node.RightChild
                        continue
                    else: 
                        return Node
            
        found = BSTFind()
        if self.Root is not None:
            if self.Root.NodeKey == key:
                found.Node = self.Root
                found.NodeHasKey = True
                return found
            else:
                node = FindNode(self.Root, key)
                if node.NodeKey == key:
                    found.Node = node
                    found.NodeHasKey = True
                    return found
                else:
                    found.Node = node
                    if node.NodeKey > key:
                        found.ToLeft = True
                    return found
        else:
            return found

    # Метод добавления ключа-значения в дерево
    def AddKeyValue(self, key, val):
        NewNode = BSTNode(key, val, None)
        Node = self.FindNodeByKey(key)
        if not Node.NodeHasKey:
            if Node.Node is None:
                self.Root = NewNode
            else:
                NewNode.Parent = Node.Node
                if Node.ToLeft:
                    Node.Node.LeftChild = NewNode
                else:
                    Node.Node.RightChild = NewNode
            return True
        else:
            return False # если ключ уже есть
  
    # Метод поиска максимального/минимального ключа в поддереве
    def FinMinMax(self, FromNode, FindMax):
        if FromNode is not None:
            ResultFindNode = FromNode
            if FindMax:
                while ResultFindNode.RightChild is not None:
                    ResultFindNode = ResultFindNode.RightChild
            else:
                while ResultFindNode.LeftChild is not None:
                    ResultFindNode = ResultFindNode.LeftChild
            return ResultFindNode
        else:
            return None
	
    # Метод удаления узла по его ключу
    def DeleteNodeByKey(self, key):

        def Delete_Node(DeleteNode):
            DeleteNode.Parent = None 
            DeleteNode.LeftChild = None 
            DeleteNode.RightChild = None 
        
        def Move_Node(DeleteNode, SuccessorNode):
            # определяем связь с родителем 
            if DeleteNode is self.Root:
                SuccessorNode.Parent = None
                self.Root = SuccessorNode
            else:
                SuccessorNode.Parent = DeleteNode.Parent 
                if DeleteNode.Parent.LeftChild == DeleteNode:
                    DeleteNode.Parent.LeftChild = SuccessorNode
                else:
                    DeleteNode.Parent.RightChild == DeleteNode
                    DeleteNode.Parent.RightChild = SuccessorNode
            if DeleteNode.LeftChild == SuccessorNode:    # если у удаляемого узла только левый потомок
                return
            if DeleteNode.LeftChild is not None:    # определяем связь с левым потомком удаляемого узла
                SuccessorNode.LeftChild = DeleteNode.LeftChild
                DeleteNode.LeftChild.Parent = SuccessorNode
            if DeleteNode.RightChild != SuccessorNode:    # определяем связь с правым потомком удаляемого узла
                SuccessorNode.RightChild = DeleteNode.RightChild
                DeleteNode.RightChild.Parent = SuccessorNode

        BSTFind_Node = self.FindNodeByKey(key)
        if BSTFind_Node.NodeHasKey is False:    # если узел не найден
            return False
        
        DeleteNode = BSTFind_Node.Node
        if DeleteNode == self.Root and DeleteNode.LeftChild is None and DeleteNode.RightChild is None:    # Если есть только корень
            Delete_Node(DeleteNode)
            self.Root = None
            return True

        # Если удаляемый узел ЛИСТ
        if DeleteNode.LeftChild is None and DeleteNode.RightChild is None:
            if DeleteNode.Parent.LeftChild == DeleteNode:
                DeleteNode.Parent.LeftChild = None
            else:
                DeleteNode.Parent.RightChild = None
            Delete_Node(DeleteNode)
            return True
    
        if DeleteNode.RightChild is None:
            Move_Node(DeleteNode, DeleteNode.LeftChild)
        elif DeleteNode.RightChild.LeftChild is None:    # если у правого потомка удаляемого узла нет левого потомка
            Move_Node(DeleteNode, DeleteNode.RightChild)
        else:
            Successor = self.FinMinMax(DeleteNode.RightChild, False)
            if Successor.RightChild is not None:
                Successor.Parent.LeftChild = Successor.RightChild
                Successor.RightChild.Parent = Successor.Parent
            elif DeleteNode.RightChild != Successor:
                Successor.Parent.LeftChild = None
            Move_Node(DeleteNode, Successor)
        Delete_Node(DeleteNode)
        return True 


    # Метод получения количества всех узлов в дереве
    def Count(self):
        if self.Root is not None:
            return len(self.__GetAllNodes(self.Root, [self.Root], [self.Root]))
        else:
            return 0


    #------------------------- Методы обхода дерева ---------------------------------------------------------
    
    # "Служебный" метод поиска всех узлов дерева (рекурсия)
    def __GetAllNodes(self, Node, list_all_nodes, visited_nodes):
        if Node.RightChild:
            list_all_nodes.append(Node.RightChild)
        if Node.LeftChild:
            list_all_nodes.append(Node.LeftChild)
        for node in list_all_nodes:
            if node not in visited_nodes:
                visited_nodes.append(node)
                self.__GetAllNodes(node, list_all_nodes, visited_nodes)
        return list_all_nodes

    #  Метод обхода дерева в ширину. Возвращает кортеж объектов класса BSTFind
    def WideAllNodes(self):
        if self.Root is None:
            return None
        # формируем список узлов дерева
        List_All_Nodes = [self.Root]
        Visited_Nodes = []
        Number_All_Nodes = 1
        Number_Visited_Nodes = 0
        while Number_All_Nodes != Number_Visited_Nodes:
            for Node in List_All_Nodes:
                if Node not in Visited_Nodes:
                    if Node.LeftChild is not None:
                        List_All_Nodes.append(Node.LeftChild)
                    if Node.RightChild is not None:
                        List_All_Nodes.append(Node.RightChild)
                    Visited_Nodes.append(Node)
            Number_Visited_Nodes = len(Visited_Nodes)
            Number_All_Nodes = len(List_All_Nodes)
        Number_Visited_Nodes = None
        return tuple(List_All_Nodes)

    #  3 метода обхода дерева в глубину (рекурсия). Возвращает кортеж объектов класса BSTFind
    def DeepAllNodes(self, order):
        def InorderTraversal(Node):
            if Node is None:
                return []
            res = []
            res.extend(InorderTraversal(Node.LeftChild))
            res.append(Node)
            res.extend(InorderTraversal(Node.RightChild))
            return res
        
        def PostorderTraversal(Node):
            if Node is None:
                return []
            res = []
            res.extend(InorderTraversal(Node.LeftChild))
            res.extend(InorderTraversal(Node.RightChild))
            res.append(Node)
            return res

        def PreorderTraversal(Node):
            if Node is None:
                return []
            res = []
            res.append(Node)
            res.extend(InorderTraversal(Node.LeftChild))
            res.extend(InorderTraversal(Node.RightChild))
            return res
        
        if self.Root is None:
            return None

        if order == 0:    # in-order: Left -> Root -> Right
            List_All_Nodes = InorderTraversal(self.Root)
        elif order == 1:    # post-order: # Left ->Right -> Root
            List_All_Nodes = PostorderTraversal(self.Root)
        elif order == 2:    # pre-order: Root -> Left ->Right
            List_All_Nodes = PreorderTraversal(self.Root)
        return tuple(List_All_Nodes)


"""node8 = BSTNode(8, 1, None)
node4 = BSTNode(4, 2, node8)
node12 = BSTNode(12, 3, node8)
node2 = BSTNode(2, 4, node4)
node6 = BSTNode(6, 5, node4)
node10 = BSTNode(10, 6, node12)
node14 = BSTNode(14, 7, node12)
node1 = BSTNode(1, 8, node2)
node3 = BSTNode(3, 9, node2)
node5 = BSTNode(5, 10, node6)
node7 = BSTNode(7, 11, node6)
node9 = BSTNode(9, 12, node10)
node11 = BSTNode(11, 13, node10)
node13 = BSTNode(13, 14, node14)
node15 = BSTNode(15, 15, node14)

node8.LeftChild = node4
node8. RightChild = node12
node4.LeftChild = node2
node4. RightChild = node6
node12.LeftChild = node10
node12. RightChild = node14
node2.LeftChild = node1
node2. RightChild = node3
node6.LeftChild = node5
node6. RightChild = node7
node10.LeftChild = node9
node10. RightChild = node11
node14.LeftChild = node13
node14. RightChild = node15

My_Tree = BST(node8)

a = []
z = My_Tree.DeepAllNodes(0)
for node in z:
    a.append(node.Node.NodeKey)
print(a)
print()"""