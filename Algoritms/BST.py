# ДЕРЕВЬЯ.
# Реализация двоичного дерева поиска.

from ast import Delete, Sub


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