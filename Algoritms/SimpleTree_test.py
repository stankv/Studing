import unittest
from SimpleTree import SimpleTreeNode, SimpleTree

class SimpleTreeTest(unittest.TestCase):

    def setUp(self):
        self.node0 = SimpleTreeNode(9, None)
        self.node1 = SimpleTreeNode(4, None)
        self.node2 = SimpleTreeNode(17, None)
        self.node3 = SimpleTreeNode(3, None)
        self.node4 = SimpleTreeNode(6, None)
        self.node5 = SimpleTreeNode(22, None)
        self.node6 = SimpleTreeNode(5, None)
        self.node7 = SimpleTreeNode(7, None)
        self.node8 = SimpleTreeNode(20, None)
        self.node9 = SimpleTreeNode(10, None)
        self.node10 = SimpleTreeNode(11, None)
        self.node11 = SimpleTreeNode(12, None)
        self.node12 = SimpleTreeNode(13, None)
        self.node13 = SimpleTreeNode(14, None)
        self.node14 = SimpleTreeNode(11, None)

        self.My_Tree = SimpleTree(self.node0)
        self.My_Tree.AddChild(self.node0, self.node1)
        self.My_Tree.AddChild(self.node0, self.node2)
        self.My_Tree.AddChild(self.node1, self.node3)
        self.My_Tree.AddChild(self.node1, self.node4)
        self.My_Tree.AddChild(self.node4, self.node6)
        self.My_Tree.AddChild(self.node4, self.node7)
        self.My_Tree.AddChild(self.node2, self.node5)
        self.My_Tree.AddChild(self.node5, self.node8)
        self.My_Tree.AddChild(self.node0, self.node9)
        self.My_Tree.AddChild(self.node9, self.node10)
        self.My_Tree.AddChild(self.node9, self.node11)
        self.My_Tree.AddChild(self.node11, self.node12)
        self.My_Tree.AddChild(self.node11, self.node13)
        self.My_Tree.AddChild(self.node11, self.node14)

    def test_AddChild(self):
        node15 = SimpleTreeNode(100, None)
        self.My_Tree.AddChild(self.node3, node15)
        self.assertIn(node15, self.node3.Children)
        self.assertEqual(self.node3, node15.Parent)

    def test_DeleteNode(self):
        self.My_Tree.DeleteNode(self.node4)
        self.assertNotIn(self.node4, self.My_Tree.GetAllNodes())
        self.assertNotIn(self.node6, self.My_Tree.GetAllNodes())
        self.assertNotIn(self.node7, self.My_Tree.GetAllNodes())

    def test_GetAllNodes(self):
        list_all_values = [9,4,17,10,3,6,5,7,22,20,11,12,13,14,11]
        list_all_nodes = self.My_Tree.GetAllNodes()
        list_all_values_test = []
        for node in list_all_nodes:
            list_all_values_test.append(node.NodeValue)
        self.assertEqual(list_all_values_test, list_all_values)

    def test_FindNodesByValue1(self):
        list_nodes = self.My_Tree.FindNodesByValue(1000)
        self.assertEqual([], list_nodes)

    def test_FindNodesByValue2(self):
        list_nodes = self.My_Tree.FindNodesByValue(11)
        list_values = []
        for node in list_nodes:
            list_values.append(node.NodeValue)
        self.assertEqual(list_values, [11,11])


    def test_MoveNode(self):
        self.My_Tree.MoveNode(self.node5, self.node3)
        self.assertEqual([self.node5], self.node3.Children)
        self.assertEqual(self.node5.Parent, self.node3)
        self.assertEqual([], self.node2.Children)

    def test_Count(self):
        self.assertEqual(self.My_Tree.Count(), 15)

    def test_LeafCount(self):
        self.assertEqual(self.My_Tree.LeafCount(), 8)

if __name__ == '__main__':
    unittest.main()