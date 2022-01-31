# ДЕРЕВЬЯ.
# Построение сбалансированного бинарного дерева поиска из данных неотсортированного массива.

from msilib.schema import CheckBox


class BSTNode:
	
    def __init__(self, key, parent):
        self.NodeKey = key # ключ узла
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
        self.Level = 0 # уровень узла
        
class BalancedBST:
		
    def __init__(self):
    	self.Root = None # корень дерева

    # создаём дерево с нуля из неотсортированного массива a
    def GenerateTree(self, a):
	
        def AddNodeToTree(parent, a, level=0):    # возвращает коренной узел!
            if a == []:
                return
            index_center = len(a) // 2
            Node = BSTNode(a[index_center], parent)
            Node.Level = level
            Node.Parent = parent
            level += 1
            Node.LeftChild = AddNodeToTree(Node, a[:index_center], level)
            Node.RightChild = AddNodeToTree(Node, a[index_center + 1:], level)
            print(Node.NodeKey)
            return Node

        if len(a) == 1:
            self.Root = BSTNode(a[0], None)
            return self.Root
        elif a == [] or a is None:
            return None
        elif len(a) > 1:
            a.sort()
            self.Root = AddNodeToTree(None, a)
            return self.Root



    def IsBalanced(self, root_node):

        def CheckBalance(root_node, difference):
            if root_node.LeftChild:
                difference += 1
                CheckBalance(root_node.LeftChild, difference)
            if root_node.RightChild:
                difference -= 1
                CheckBalance(root_node.RightChild, difference)
        
        if root_node is None:
            return False
        difference = 0
        CheckBalance(root_node, difference)
        if difference >= 0 and difference <= 1:
            return True
        else:
            return False


"""z = [7,2,3,1,4,8,9,6,10,5,0]
My_Tree = BalancedBST()
node = My_Tree.GenerateTree(z)
print()
print("node:", node.NodeKey, "parent:", node.Parent, 'level:', node.Level)
print("left:", node.LeftChild.NodeKey, "right:", node.RightChild.NodeKey)
print(node.LeftChild.Parent.NodeKey, node.RightChild.Parent.NodeKey)
print()
node = node.LeftChild
print("node:", node.NodeKey, "parent:", node.Parent.NodeKey, 'level:', node.Level)
print("left:", node.LeftChild.NodeKey, "right:", node.RightChild.NodeKey)
print(node.LeftChild.Parent.NodeKey, node.RightChild.Parent.NodeKey)
print()
node = node.Parent.RightChild
print("node:", node.NodeKey, "parent:", node.Parent.NodeKey, 'level:', node.Level)
print("left:", node.LeftChild.NodeKey, "right:", node.RightChild.NodeKey)
print(node.LeftChild.Parent.NodeKey, node.RightChild.Parent.NodeKey)
print(My_Tree.IsBalanced(My_Tree.Root))"""