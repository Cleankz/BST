import unittest
import random
from BST import BSTNode,BSTFind,BST

class MyTests(unittest.TestCase):

    def test_delete_node(self):
        # проверяем что дерево пустое и в нем нет узлов
        root = BSTNode(20,random.randint(0,50),None)
        tree = BST(root)
        self.assertEqual(tree.DeleteNodeByKey(20),True)# возвращает False если  не удалось удалить корень
        self.assertEqual(tree.Root,None)
        self.assertEqual(tree.Count(),0) # число узлов в дереве

        tree = BST(root)
        tree.AddKeyValue(19,random.randint(0,50))
        tree.AddKeyValue(21,random.randint(0,50))
        self.assertEqual(tree.Count(),3)

        # проверяем удаление кореного узла
        self.assertEqual(tree.DeleteNodeByKey(20),True)
        self.assertEqual(tree.Count(),2)
        self.assertEqual(tree.Root.NodeKey,21)

        #проверяем удаление левого и правого потомка кореного узла
        tree.AddKeyValue(22,random.randint(0,50))
        self.assertEqual(tree.DeleteNodeByKey(19),True)
        self.assertEqual(tree.Count(),2)
        self.assertEqual(tree.Root.LeftChild,None)

        self.assertEqual(tree.DeleteNodeByKey(22),True)
        self.assertEqual(tree.Root.RightChild,None)
        self.assertEqual(tree.Count(),1)

        #проверяем удаление правого потомка имеющего два подкорня
        tree.AddKeyValue(25,random.randint(0,50))
        tree.AddKeyValue(24,random.randint(0,50))
        tree.AddKeyValue(26,random.randint(0,50))

        self.assertEqual(tree.DeleteNodeByKey(25),True)
        self.assertEqual(tree.Root.RightChild.NodeKey,26)
        self.assertEqual(tree.Root.RightChild.LeftChild.NodeKey,24)

        #проверяем удаление левого потомка имеющего два подкорня
        tree.AddKeyValue(12,random.randint(0,50))
        tree.AddKeyValue(15,random.randint(0,50))
        tree.AddKeyValue(10,random.randint(0,50))

        self.assertEqual(tree.DeleteNodeByKey(12),True)
        self.assertEqual(tree.Root.LeftChild.NodeKey,15)
        self.assertEqual(tree.Root.LeftChild.LeftChild.NodeKey,10)

        #проверяем удаление левого потомка имеющего один левый подкорень
        self.assertEqual(tree.DeleteNodeByKey(15),True)
        self.assertEqual(tree.Root.LeftChild.NodeKey,10)

        #проверяем удаление левого потомка имеющего один правый подкорень
        tree.AddKeyValue(11,random.randint(0,50))
        self.assertEqual(tree.DeleteNodeByKey(10),True)
        self.assertEqual(tree.Root.LeftChild.NodeKey,11)

        #проверяем удаление правого потомка имеющего один левый подкорень
        self.assertEqual(tree.DeleteNodeByKey(26),True)
        self.assertEqual(tree.Root.RightChild.NodeKey,24)

        #проверяем удаление правого потомка имеющего один правый подкорень
        tree.AddKeyValue(27,random.randint(0,50))
        self.assertEqual(tree.DeleteNodeByKey(24),True)
        self.assertEqual(tree.Root.RightChild.NodeKey,27)

    def test_add_key_value(self):
        root = BSTNode(20,random.randint(0,50),None)
        tree = BST(root)
        self.assertEqual(tree.AddKeyValue(19,random.randint(0,50)),True)
        tree.AddKeyValue(21,random.randint(0,50))
        self.assertEqual(tree.AddKeyValue(21,random.randint(0,50)),False)# возвращает False если ключ уже есть
        self.assertEqual(tree.Count(),3)

    def test_addKeyValue_zero(self):
        root = BSTNode(20,random.randint(0,50),None)
        tree = BST(root)
        self.assertEqual(tree.Count(),1)
        tree.DeleteNodeByKey(20)
        self.assertEqual(tree.Count(),0)
        tree.AddKeyValue(50,6)

    def test_findByKey(self):
        root = BSTNode(20,random.randint(0,50),None)
        tree = BST(root)
        self.assertEqual(tree.FindNodeByKey(20).NodeHasKey,True)
        self.assertEqual(tree.FindNodeByKey(50566).NodeHasKey,False)

    def test_count(self):
        root = BSTNode(8,random.randint(0,50),None)
        tree = BST(root)
        self.assertEqual(tree.Count(),1) # проверяем что узел 1


        tree.AddKeyValue(4,random.randint(0,50))
        tree.AddKeyValue(12,random.randint(0,50))
        tree.AddKeyValue(2,random.randint(0,50))
        tree.AddKeyValue(6,random.randint(0,50))
        tree.AddKeyValue(1,random.randint(0,50))
        tree.AddKeyValue(3,random.randint(0,50))
        tree.AddKeyValue(5,random.randint(0,50))
        tree.AddKeyValue(7,random.randint(0,50))
        tree.AddKeyValue(10,random.randint(0,50))
        tree.AddKeyValue(14,random.randint(0,50))
        tree.AddKeyValue(9,random.randint(0,50))
        tree.AddKeyValue(11,random.randint(0,50))
        tree.AddKeyValue(13,random.randint(0,50))
        tree.AddKeyValue(15,random.randint(0,50))
        self.assertEqual(tree.Count(),15)
        tree.DeleteNodeByKey(1)
        tree.DeleteNodeByKey(12)
        self.assertEqual(tree.Count(),13)

if __name__ == '__main__':
    unittest.main()