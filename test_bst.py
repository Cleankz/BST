import unittest
import random
from BST import BSTNode,BSTFind,BST

class MyTests(unittest.TestCase):

    def test_delete_node(self):
        root = BSTNode(20,random.randint(0,50),None)
        tree = BST(root)
        tree.AddKeyValue(19,random.randint(0,50))
        tree.AddKeyValue(21,random.randint(0,50))
        self.assertEqual(tree.Count(),3)

        # проверяем удаление кореного узла
        tree.DeleteNodeByKey(20)
        self.assertEqual(tree.Count(),2)
        self.assertEqual(tree.Root.NodeKey,21)

        #проверяем удаление левого и правого потомка кореного узла
        tree.AddKeyValue(22,random.randint(0,50))
        tree.DeleteNodeByKey(19)
        self.assertEqual(tree.Count(),2)
        self.assertEqual(tree.Root.LeftChild,None)

        tree.DeleteNodeByKey(22)
        self.assertEqual(tree.Root.RightChild,None)
        self.assertEqual(tree.Count(),1)

        #проверяем удаление правого потомка имеющего два подкорня
        tree.AddKeyValue(25,random.randint(0,50))
        tree.AddKeyValue(24,random.randint(0,50))
        tree.AddKeyValue(26,random.randint(0,50))

        tree.DeleteNodeByKey(25)
        self.assertEqual(tree.Root.RightChild.NodeKey,26)
        self.assertEqual(tree.Root.RightChild.LeftChild.NodeKey,24)

        #проверяем удаление левого потомка имеющего два подкорня
        tree.AddKeyValue(12,random.randint(0,50))
        tree.AddKeyValue(15,random.randint(0,50))
        tree.AddKeyValue(10,random.randint(0,50))

        tree.DeleteNodeByKey(12)
        self.assertEqual(tree.Root.LeftChild.NodeKey,15)
        self.assertEqual(tree.Root.LeftChild.LeftChild.NodeKey,10)

        #проверяем удаление левого потомка имеющего один левый подкорень
        tree.DeleteNodeByKey(15)
        self.assertEqual(tree.Root.LeftChild.NodeKey,10)

        #проверяем удаление левого потомка имеющего один правый подкорень
        tree.AddKeyValue(11,random.randint(0,50))
        tree.DeleteNodeByKey(10)
        self.assertEqual(tree.Root.LeftChild.NodeKey,11)

        #проверяем удаление правого потомка имеющего один левый подкорень
        tree.DeleteNodeByKey(26)
        self.assertEqual(tree.Root.RightChild.NodeKey,24)

        #проверяем удаление правого потомка имеющего один правый подкорень
        tree.AddKeyValue(27,random.randint(0,50))
        tree.DeleteNodeByKey(24)
        self.assertEqual(tree.Root.RightChild.NodeKey,27)

if __name__ == '__main__':
    unittest.main()