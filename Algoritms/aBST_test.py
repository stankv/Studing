import unittest
from aBST import aBST

class aBST_Test(unittest.TestCase):
    def setUp(self):
        self.My_Tree = aBST(3)
        self.My_Tree_None = aBST(0)

    def test_both_functions(self):
        index0 = self.My_Tree.FindKeyIndex(0)
        index50 = self.My_Tree.FindKeyIndex(50)
        self.assertEqual(index0, 0)
        self.assertEqual(index50, 0)
        
        index_add50 = self.My_Tree_None.AddKey(50)
        index_add75 = self.My_Tree_None.AddKey(75)
        self.assertEqual(index_add50, 0)
        self.assertEqual(index_add75, -1)
        
        self.My_Tree.AddKey(50)
        index_add75 = self.My_Tree.AddKey(75)
        self.assertEqual(index_add75, 2)
        index_add25 = self.My_Tree.AddKey(25)
        self.assertEqual(index_add25, 1)

        self.My_Tree.AddKey(62)
        self.My_Tree.AddKey(37)
        self.My_Tree.AddKey(55)
        self.My_Tree.AddKey(43)
        self.My_Tree.AddKey(31)
        self.My_Tree.AddKey(84)
        self.My_Tree.AddKey(92)
        self.assertEqual(self.My_Tree.Tree, [50, 25, 75, None, 37, 62, 84, None, None, 31, 43, 55, None, None, 92])

if __name__ == '__main__':
    unittest.main()