import unittest
from SimpleGraph import *

class DefTast(unittest.TestCase):

    def setUp(self):
        self.My_SimpleGrap0 = SimpleGraph(0)
        self.My_SimpleGrap1 = SimpleGraph(1)
        self.My_SimpleGrap10 = SimpleGraph(10)

    def test_SimpleGrap0(self):
        self.My_SimpleGrap0.AddVertex(100)
        self.assertEqual(self.My_SimpleGrap0.max_vertex, 0)
        self.assertEqual(self.My_SimpleGrap0.vertex, [])

        self.My_SimpleGrap0.AddEdge(1, 2)
        self.assertEqual(self.My_SimpleGrap0.IsEdge(1, 2), False)

        self.My_SimpleGrap0.RemoveVertex(0)
        self.assertEqual(self.My_SimpleGrap0.vertex, [])

    def test_SimpleGrap1(self):
        self.My_SimpleGrap1.AddVertex(100)
        self.assertEqual(self.My_SimpleGrap1.max_vertex, 1)
        self.assertEqual(self.My_SimpleGrap1.vertex[0].Value, 100)

        self.My_SimpleGrap1.AddEdge(1, 2)
        self.assertEqual(self.My_SimpleGrap1.IsEdge(1, 2), False)

        self.My_SimpleGrap1.AddEdge(0, 0)
        self.assertEqual(self.My_SimpleGrap1.IsEdge(0, 0), True)

        self.My_SimpleGrap1.RemoveVertex(0)
        self.assertEqual(self.My_SimpleGrap1.vertex, [None])
        self.assertEqual(self.My_SimpleGrap1.IsEdge(0, 0), False)

    def test_SimpleGrap10(self):
        self.My_SimpleGrap10.AddVertex(1)
        self.My_SimpleGrap10.AddVertex(2)
        self.My_SimpleGrap10.AddVertex(3)
        self.My_SimpleGrap10.AddVertex(4)
        self.My_SimpleGrap10.AddVertex(5)
        self.My_SimpleGrap10.AddVertex(6)
        self.assertEqual(self.My_SimpleGrap10.max_vertex, 10)
        self.assertEqual(self.My_SimpleGrap10.vertex[0].Value, 1)
        self.assertEqual(self.My_SimpleGrap10.vertex[1].Value, 2)
        self.assertEqual(self.My_SimpleGrap10.vertex[2].Value, 3)
        self.assertEqual(self.My_SimpleGrap10.vertex[3].Value, 4)
        self.assertEqual(self.My_SimpleGrap10.vertex[4].Value, 5)
        self.assertEqual(self.My_SimpleGrap10.vertex[5].Value, 6)
        
        self.My_SimpleGrap10.AddEdge(1, 2)
        self.assertEqual(self.My_SimpleGrap10.IsEdge(1, 2), True)
        self.assertEqual(self.My_SimpleGrap10.IsEdge(2, 1), True)

        self.My_SimpleGrap10.AddEdge(1, 3)
        self.assertEqual(self.My_SimpleGrap10.IsEdge(1, 3), True)
        self.assertEqual(self.My_SimpleGrap10.IsEdge(3, 1), True)

        self.My_SimpleGrap10.AddEdge(2, 3)
        self.assertEqual(self.My_SimpleGrap10.IsEdge(2, 3), True)
        self.assertEqual(self.My_SimpleGrap10.IsEdge(3, 2), True)

        self.assertEqual(self.My_SimpleGrap10.IsEdge(0, 0), False)

        self.My_SimpleGrap10.RemoveVertex(1)
        self.assertEqual(self.My_SimpleGrap10.IsEdge(1, 2), False)
        self.assertEqual(self.My_SimpleGrap10.IsEdge(2, 1), False)
        self.assertEqual(self.My_SimpleGrap10.IsEdge(1, 3), False)
        self.assertEqual(self.My_SimpleGrap10.IsEdge(3, 1), False)
        self.assertEqual(self.My_SimpleGrap10.IsEdge(2, 3), True)
        self.assertEqual(self.My_SimpleGrap10.IsEdge(3, 2), True)

        self.My_SimpleGrap10.RemoveEdge(3, 2)
        self.assertEqual(self.My_SimpleGrap10.IsEdge(2, 3), False)
        self.assertEqual(self.My_SimpleGrap10.IsEdge(3, 2), False)

if __name__ == '__main__':
    unittest.main()