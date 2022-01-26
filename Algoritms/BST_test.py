import unittest
from BST import BSTNode, BSTFind, BST

class SimpleTreeTest(unittest.TestCase):

    def setUp(self):
        self.node8 = BSTNode(8, 1, None)
        self.node4 = BSTNode(4, 2, self.node8)
        self.node12 = BSTNode(12, 3, self.node8)
        self.node2 = BSTNode(2, 4, self.node4)
        self.node6 = BSTNode(6, 5, self.node4)
        self.node10 = BSTNode(10, 6, self.node12)
        self.node14 = BSTNode(14, 7, self.node12)
        self.node1 = BSTNode(1, 8, self.node2)
        self.node3 = BSTNode(3, 9, self.node2)
        self.node5 = BSTNode(5, 10, self.node6)
        self.node7 = BSTNode(7, 11, self.node6)
        self.node9 = BSTNode(9, 12, self.node10)
        self.node11 = BSTNode(11, 13, self.node10)
        self.node13 = BSTNode(13, 14, self.node14)
        self.node15 = BSTNode(15, 15, self.node14)

        self.node8.LeftChild = self.node4
        self.node8. RightChild = self.node12
        self.node4.LeftChild = self.node2
        self.node4. RightChild = self.node6
        self.node12.LeftChild = self.node10
        self.node12. RightChild = self.node14
        self.node2.LeftChild = self.node1
        self.node2. RightChild = self.node3
        self.node6.LeftChild = self.node5
        self.node6. RightChild = self.node7
        self.node10.LeftChild = self.node9
        self.node10. RightChild = self.node11
        self.node14.LeftChild = self.node13
        self.node14. RightChild = self.node15

        self.My_Tree = BST(self.node8)

    def test_Count(self):
        self.assertEqual(self.My_Tree.Count(), 15)

    def test_FindNodeByKey(self):
        test_BSTFind_0 = self.My_Tree.FindNodeByKey(0)
        test_BSTFind_16 = self.My_Tree.FindNodeByKey(16)
        test_BSTFind_Root = self.My_Tree.FindNodeByKey(8)
        test_BSTFind_6 = self.My_Tree.FindNodeByKey(6)

        # Ключ не существует, добавление к Node_1, левый потомок
        self.assertEqual(test_BSTFind_0.NodeHasKey, False)
        self.assertEqual(test_BSTFind_0.ToLeft, True)
        self.assertEqual(test_BSTFind_0.Node, self.node1)

        # Ключ не существует, добавление к Node_15, правый потомок
        self.assertEqual(test_BSTFind_16.NodeHasKey, False)
        self.assertEqual(test_BSTFind_16.ToLeft, False)
        self.assertEqual(test_BSTFind_16.Node, self.node15)

        # Ключ существует и является корнем
        self.assertEqual(test_BSTFind_Root.NodeHasKey, True)
        self.assertEqual(test_BSTFind_Root.ToLeft, False)
        self.assertEqual(test_BSTFind_Root.Node, self.node8)
    
        # Ключ существует
        self.assertEqual(test_BSTFind_6.NodeHasKey, True)
        self.assertEqual(test_BSTFind_6.ToLeft, False)
        self.assertEqual(test_BSTFind_6.Node, self.node6)

    def test_FinMinMax(self):
        min_root = self.My_Tree.FinMinMax(self.My_Tree.Root, False)
        max_root = self.My_Tree.FinMinMax(self.My_Tree.Root, True)
        self.assertEqual(min_root, self.node1)
        self.assertEqual(max_root, self.node15)

        min_Node_4 = self.My_Tree.FinMinMax(self.node4, False)
        max_Node_4 = self.My_Tree.FinMinMax(self.node4, True)
        self.assertEqual(min_Node_4, self.node1)
        self.assertEqual(max_Node_4, self.node7)

        min_Node_12 = self.My_Tree.FinMinMax(self.node12, False)
        max_Node_12 = self.My_Tree.FinMinMax(self.node12, True)
        self.assertEqual(min_Node_12, self.node9)
        self.assertEqual(max_Node_12, self.node15)

        min_Node_11 = self.My_Tree.FinMinMax(self.node11, False)
        max_Node_11 = self.My_Tree.FinMinMax(self.node11, True)
        self.assertEqual(min_Node_11, max_Node_11)

    def test_AddKeyValue(self):
        #  добавление в пустое дерево
        self.My_Tree_empty = BST(None)
        self.assertEqual(self.My_Tree_empty.Count(), 0)
        self.My_Tree_empty.AddKeyValue(1, 11)
        self.assertEqual(self.My_Tree_empty.Count(), 1)
        self.assertEqual(self.My_Tree_empty.FindNodeByKey(1).NodeHasKey, True)
        self.assertEqual(self.My_Tree_empty.Root.NodeKey, 1)

        # удаляем узел 6, тогда вместо узла 6 встанет узел 7 (с потомком узел 5)
        self.assertEqual(self.My_Tree.Count(), 15)
        self.My_Tree.DeleteNodeByKey(6)
        BSTFind_Del_6 = self.My_Tree.FindNodeByKey(6)
        self.assertEqual(BSTFind_Del_6.NodeHasKey, False)
        self.assertEqual(self.My_Tree.Count(), 14)

        # Добавляем узел правым потомком
        self.My_Tree.AddKeyValue(6, 60)
        BSTFind_Add_6 = self.My_Tree.FindNodeByKey(6)
        self.assertEqual(BSTFind_Add_6.NodeHasKey, True)
        self.assertEqual(BSTFind_Add_6.Node.NodeValue, 60)
        self.assertEqual(self.node7.LeftChild.NodeKey, 5)
        self.assertEqual(BSTFind_Add_6.Node.Parent.NodeKey, 5)    # родителем узла 6 будет узел 5
        self.assertEqual(self.node5.RightChild, BSTFind_Add_6.Node)    # правым потомком узла 5 будет узел 6
        self.assertEqual(self.My_Tree.Count(), 15)

        # добавляем узел левым потомком
        self.assertEqual(self.My_Tree.FindNodeByKey(0).NodeHasKey, False) # проверка что в дереве нет узла с этим ключом
        self.My_Tree.AddKeyValue(0, 0)
        BSTFind_Add_0 = self.My_Tree.FindNodeByKey(0)
        self.assertEqual(BSTFind_Add_0.NodeHasKey, True)
        self.assertEqual(BSTFind_Add_0.Node.NodeValue, 0)
        self.assertEqual(BSTFind_Add_0.Node.Parent.NodeKey, 1)    # родителем узла 0 будет узел 1
        self.assertEqual(self.node1.LeftChild, BSTFind_Add_0.Node) # левым потомком узла 1 будет узел 0
        self.assertEqual(self.My_Tree.Count(), 16)

        # попытка добавить узел, который уже есть в дереве
        self.assertEqual(self.My_Tree.FindNodeByKey(8).NodeHasKey, True)    # проверка что в дереве есть узел с этим ключом 
        self.My_Tree.AddKeyValue(8, 0)
        BSTFind_Add_8 = self.My_Tree.FindNodeByKey(8)
        self.assertEqual(BSTFind_Add_8.NodeHasKey, True)
        self.assertEqual(BSTFind_Add_8.Node.LeftChild, self.node4)
        self.assertEqual(BSTFind_Add_8.Node.RightChild, self.node12)
        self.assertEqual(self.node8, self.My_Tree.Root)
        self.assertEqual(self.My_Tree.Count(), 16)


    def test_DeleteNodeByKey(self):
        # Удаляем корень
        self.My_Tree.DeleteNodeByKey(8)
        self.assertEqual(self.My_Tree.Root.NodeKey, self.node9.NodeKey)
        self.assertEqual(self.node9.LeftChild, self.node4)
        self.assertEqual(self.node9.RightChild, self.node12)
        self.assertEqual(self.node4.Parent.NodeKey, self.node9.NodeKey)
        self.assertEqual(self.node12.Parent, self.node9)
        self.assertEqual(self.node10.LeftChild, None)
        self.assertEqual(self.My_Tree.Count(), 14)

        # удаляем левый лист
        self.My_Tree.DeleteNodeByKey(13)
        self.assertEqual(self.node14.LeftChild, None)
        self.assertEqual(self.My_Tree.Count(), 13)

        # удаляем правый лист
        self.My_Tree.DeleteNodeByKey(11)
        self.assertEqual(self.node10.RightChild, None)
        self.assertEqual(self.My_Tree.Count(), 12)

        self.My_Tree.DeleteNodeByKey(1)
        self.assertEqual(self.node2.LeftChild, None)
        self.assertEqual(self.My_Tree.Count(), 11)

        self.My_Tree.DeleteNodeByKey(2)
        self.assertEqual(self.node4.LeftChild, self.node3)
        self.assertEqual(self.node3.Parent, self.node4)

        self.My_Tree.DeleteNodeByKey(3)
        self.assertEqual(self.node4.LeftChild, None)

        self.My_Tree.DeleteNodeByKey(4)
        self.assertEqual(self.node5.Parent.NodeKey, self.node9.NodeKey)
        self.assertEqual(self.node5.LeftChild, None)
        self.assertEqual(self.node5.RightChild, self.node6)
        self.assertEqual(self.node9.LeftChild, self.node5)
        self.assertEqual(self.node6.Parent.NodeKey, self.node5.NodeKey)
        self.assertEqual(self.node6.LeftChild, None)

        self.My_Tree.DeleteNodeByKey(5)
        self.assertEqual(self.node6.Parent.NodeKey, self.node9.NodeKey)
        self.assertEqual(self.node6.RightChild.NodeKey, self.node7.NodeKey)
        self.assertEqual(self.My_Tree.Root.NodeKey, self.node9.NodeKey)
        
        self.My_Tree.DeleteNodeByKey(6)
        self.assertEqual(self.node7.Parent.NodeKey, self.node9.NodeKey)
        self.assertEqual(self.node9.LeftChild.NodeKey, self.node7.NodeKey)
        self.assertEqual(self.My_Tree.Count(), 6)

        self.My_Tree.DeleteNodeByKey(7)
        self.assertEqual(self.node9.LeftChild, None)
        
        self.My_Tree.DeleteNodeByKey(9)
        self.assertEqual(self.My_Tree.Root.NodeKey, self.node10.NodeKey)
        self.assertEqual(self.node10.LeftChild, None)
        self.assertEqual(self.node10.Parent, None)
        self.assertEqual(self.node12.Parent.NodeKey, self.node10.NodeKey)
        self.assertEqual(self.node10.RightChild.NodeKey, self.node12.NodeKey)
        self.assertEqual(self.node12.LeftChild, None)

        self.My_Tree.DeleteNodeByKey(12)
        self.assertEqual(self.node10.RightChild.NodeKey, self.node14.NodeKey)
        self.assertEqual(self.node14.Parent.NodeKey, self.node10.NodeKey)

        self.My_Tree.DeleteNodeByKey(10)
        self.assertEqual(self.My_Tree.Root.NodeKey, self.node14.NodeKey)
        self.assertEqual(self.node14.LeftChild, None)
        self.assertEqual(self.node14.Parent, None)
        self.assertEqual(self.node10.RightChild, None)
        self.assertEqual(self.node14.RightChild, self.node15)

        self.My_Tree.DeleteNodeByKey(14)
        self.assertEqual(self.My_Tree.Root.NodeKey, self.node15.NodeKey)
        self.assertEqual(self.node15.LeftChild, None)
        self.assertEqual(self.node15.Parent, None)
        self.assertEqual(self.node15.RightChild, None)
        self.assertEqual(self.My_Tree.Count(), 1)
        
        self.My_Tree.DeleteNodeByKey(15)
        self.assertEqual(self.My_Tree.Root, None)
        self.assertEqual(self.My_Tree.Count(), 0)


if __name__ == '__main__':
    unittest.main()