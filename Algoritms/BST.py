# ДЕРЕВЬЯ.
# Реализация двоичного дерева поиска.

from ast import Delete


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
        DeleteNode = self.FindNodeByKey(key)
        if DeleteNode.NodeHasKey:    # если узел найден
            if DeleteNode.Node == self.Root:    # если найденный узел корневой
                if DeleteNode.Node.LeftChild is None and DeleteNode.Node.RightChild is None:    # если узел не имеет потомков
                    self.Root = None
                    return True
                elif DeleteNode.Node.LeftChild is not None or DeleteNode.Node.RightChild is not None:    # если есть только 1 потомок
                    if DeleteNode.Node.LeftChild is not None:
                        node = DeleteNode.Node.LeftChild 
                        if node.LeftChild is None and node.RightChild is None:    # и этот потомок не имеет потомков
                            self.Root = node
                            return True
                        else:
                            return False    # если потомок имеет потомка, то удаление узла не производится
                    elif DeleteNode.Node.RightChild is not None:
                        node = DeleteNode.Node.RightChild 
                        if node.LeftChild is None and node.RightChild is None:
                            self.Root = node
                            return True
                        else:
                            return False    # если потомок имеет потомка, то не удаление узла не производится
                    else:
                        self.Root = DeleteNode.Node.RightChild
                        return True
                elif DeleteNode.Node.LeftChild is not None and DeleteNode.Node.RightChild is not None:    # если 2 потомока
                    return False    # если найденный узел корневой и имеет 2 потомка, то узел не удаляется
            elif DeleteNode.Node != self.Root:    # если найденный узел НЕ корневой
                if DeleteNode.Node.LeftChild is None and DeleteNode.Node.RightChild is None:    # и если это лист
                    DeleteNode.Node.Parent = None
                    DeleteNode.Node = None
                    return True
                elif DeleteNode.Node.LeftChild is not None or DeleteNode.Node.RightChild is not None:    # если не лист
                    if DeleteNode.Node.LeftChild is not None:                                            # и есть 1 потомок
                        DeleteNode.Node.LeftChild.Parent = DeleteNode.Node.Parent
                        DeleteNode.Node.Parent = None
                        DeleteNode.Node = None
                        return True
                    else:
                        DeleteNode.Node.RightChild.Parent = DeleteNode.Node.Parent
                        DeleteNode.Node.Parent = None
                        DeleteNode.Node = None
                        return True
                elif DeleteNode.Node.LeftChild is not None and DeleteNode.Node.RightChild is not None:    # если не лист
                    node = DeleteNode.Node.RightChild                                                     # и имеет 2 потомков
                    if node.LeftChild is None:
                        node.Parent = DeleteNode.Node.Parent
                        DeleteNode.Node.Parent = None
                        DeleteNode.Node = None
                        return True
                    else:
                        while node.LeftChild is not None:
                            node = node.LeftChild
                        node.Parent = DeleteNode.Node.Parent
                        DeleteNode.Node.Parent = None
                        DeleteNode.Node = None
                        return True
        else:
            return False # если узел не найден

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

print(My_Tree.Count())
print()
z = My_Tree.FindNodeByKey(20)
print('key: ', z.Node.NodeKey)
print('value: ', z.Node.NodeValue)
print('NodeHasKey: ', z.NodeHasKey)
print('ToLeft: ', z.ToLeft)"""
