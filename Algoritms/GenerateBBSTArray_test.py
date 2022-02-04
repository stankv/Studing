import unittest
from GenerateBBSTArray import *

class GenerateBBSTArrayTest(unittest.TestCase):

    def test_List_Empty(self):
        z = []
        self.assertEqual(GenerateBBSTArray(z), None)

    def test_List_One(self):
        z = [1]
        self.assertEqual(GenerateBBSTArray(z), [1])

    def test_List1(self):
        z = [1,2,3,4]
        self.assertEqual(GenerateBBSTArray(z), [3, 2, 4, 1, None, None, None])

    def test_List2(self):
        z = [7,2,3,1,4,8,9,6,10,5,0]
        self.assertEqual(GenerateBBSTArray(z), [5, 2, 8, 1, 4, 7, 10, 0, None, 3, None, 6, None, 9, None])

    def test_List3(self):
        z = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        res = [10,5,16,2,8,13,19,1,4,7,9,12,15,18,20,0,None,3,None,6,None,None,None,11,None,14,None,17,None,None,None]
        self.assertEqual(GenerateBBSTArray(z), res)

if __name__ == '__main__':
    unittest.main()