import random
from xmlrpc.client import Boolean, boolean
import typing
class BSTNode:

    def __init__(self, key, val,parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


class BSTFind: # промежуточный результат поиска

    def __init__(self):
        self.Node = None # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node # корень дерева, или None


    def FindByKey_node(self, key, node) -> list:
        if key == node.NodeKey:
            return [node, True, False]

        if node.LeftChild is not None and key < node.NodeKey:
            return self.FindByKey_node(key, node.LeftChild)

        elif node.RightChild is not None and key >= node.NodeKey:
            return self.FindByKey_node(key, node.RightChild)

        elif node.LeftChild is None and key < node.NodeKey:
            return [node, False, True]

        elif node.RightChild is None and key >= node.NodeKey:
            return [node, False, False]


    def FindNodeByKey(self, key) -> list:
        # ищем в дереве узел и сопутствующую информацию по ключу
        # return None # возвращает BSTFind

        find_node = self.FindByKey_node(key, self.Root)
        BSTFnd = BSTFind()

        BSTFnd.Node = find_node[0]
        BSTFnd.NodeHasKey = find_node[1]
        BSTFnd.ToLeft = find_node[2]

        find_node_list = []
        find_node_list.append(BSTFnd.Node)
        find_node_list.append(BSTFnd.NodeHasKey)
        find_node_list.append(BSTFnd.ToLeft)
        return BSTFnd

    def init_new_node(self, new_key, new_val, new_parent, ToLeft) -> None:
        new_node = BSTNode(new_key, new_val, new_parent)
        if ToLeft == True:
            new_parent.LeftChild = new_node
        else:
            new_parent.RightChild = new_node


    def AddKeyValue(self, key, val) -> boolean:
        # добавляем ключ-значение в дерево
        if self.Root == None:
            self.Root = BSTNode(key,val,None)
            return True
        find_node_list = self.FindNodeByKey(key)
        if find_node_list.NodeHasKey == False:
            self.init_new_node(key, val, find_node_list.Node, find_node_list.ToLeft)

        if find_node_list.NodeHasKey == True:
            return False # если ключ уже есть
        return True

    def FinMinMax(self, FromNode, FindMax) -> BSTNode:
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        if FindMax is True and FromNode.RightChild is not None:
            return self.FinMinMax(FromNode.RightChild, FindMax)
        elif FindMax is True and FromNode.RightChild is None:
            return FromNode

        elif FindMax == False and FromNode.LeftChild is not None:
            return self.FinMinMax(FromNode.LeftChild, FindMax)
        elif FindMax == False and FromNode.LeftChild is None:
            return FromNode

    def DeleteNodeByKey(self, key)-> boolean:
        # удаляем узел по ключу
        if self.Root == None:
            return False
        delet_node = self.FindNodeByKey(key)
        if delet_node.NodeHasKey == True:
            delet_node = delet_node.Node

            # если удаляем правый подкорень и есть только правый потомок
            if delet_node.Parent is not None \
                and delet_node.RightChild is not None \
                and delet_node.LeftChild is None\
                and delet_node.Parent.LeftChild is None: # правый подкорень
                delet_node.Parent.RightChild = delet_node.RightChild
                delet_node.RightChild.Parent = delet_node.Parent
                return True

            # если удаляем левый подкорень и есть только правый потомок
            elif delet_node.Parent is not None \
                and delet_node.RightChild is not None \
                and delet_node.LeftChild is None\
                and delet_node.Parent.RightChild is None: # левый подкорень
                delet_node.Parent.LeftChild = delet_node.RightChild
                delet_node.RightChild.Parent = delet_node.Parent
                return True

            elif delet_node.Parent is not None \
                and delet_node.RightChild is not None \
                and delet_node.LeftChild is None\
                and delet_node.Parent.RightChild is None: # левый подкорень
                delet_node.Parent.LeftChild = delet_node.RightChild
                delet_node.RightChild.Parent = delet_node.Parent
                return True

            # если удаляем правый подкорень и есть только левый потомок
            elif delet_node.Parent is not None\
                and delet_node.RightChild is None \
                and delet_node.LeftChild is not None\
                and delet_node.Parent.LeftChild is None: # правый подкорень
                delet_node.Parent.RightChild = delet_node.LeftChild
                delet_node.LeftChild.Parent = delet_node.Parent
                return True

            # если удаляем левый подкорень и есть только левый потомок
            elif delet_node.Parent is not None\
                and delet_node.RightChild is None\
                and delet_node.LeftChild is not None\
                and delet_node.Parent.RightChild is None: # левый подкорень
                delet_node.Parent.LeftChild = delet_node.LeftChild
                delet_node.LeftChild.Parent = delet_node.Parent
                return True


            # если удаляем единственный! корень и есть только правый потомок
            elif delet_node.Parent is None\
                and delet_node.RightChild is not None\
                and delet_node.LeftChild is None:
                self.Root = delet_node.RightChild
                delet_node.RightChild.Parent = None
                return True

            # если удаляем единственный!корень и есть только левый потомок
            elif delet_node.Parent is None\
                and delet_node.RightChild is None\
                and delet_node.LeftChild is not None:
                self.Root = delet_node.LeftChild
                delet_node.LeftChild.Parent = None
                return True

            elif delet_node.Parent is not None\
                and delet_node.RightChild is None\
                and delet_node.LeftChild is None\
                and delet_node.Parent.LeftChild == delet_node:
                    delet_node.Parent.LeftChild = None
                    return True

            elif delet_node.Parent is not None\
                and delet_node.RightChild is None\
                and delet_node.LeftChild is None\
                and delet_node.Parent.RightChild == delet_node:
                    delet_node.Parent.RightChild = None
                    return True


            # если удаляем корень и нет потомков
            elif delet_node.Parent is None \
                and delet_node.RightChild is None \
                and delet_node.LeftChild is None:
                self.Root = None
                return True


            # ? если удаляем левый подкорень и есть оба потомка
            elif delet_node.Parent is not None\
                and delet_node.RightChild is not None\
                and delet_node.LeftChild is not None\
                and delet_node.NodeKey < delet_node.Parent.NodeKey: # левый подкорень
                new_node = self.FinMinMax(delet_node.RightChild, False)
                new_node.Parent = delet_node.Parent
                new_node.LeftChild = delet_node.LeftChild
                delet_node.LeftChild.Parent = new_node
                delet_node.Parent.LeftChild = new_node
                return True

            #  если удаляем правый подкорень и есть оба потомка
            elif delet_node.Parent is not None\
                and delet_node.RightChild is not None\
                and delet_node.LeftChild is not None\
                and delet_node.NodeKey > delet_node.Parent.NodeKey: # правый подкорень
                new_node = self.FinMinMax(delet_node.RightChild, False)
                new_node.Parent = delet_node.Parent
                new_node.LeftChild = delet_node.LeftChild
                delet_node.LeftChild.Parent = new_node
                delet_node.Parent.RightChild = new_node
                return True


            # 10  если удаляем корень и есть оба потомка
            elif delet_node.Parent is None\
                and delet_node.RightChild is not None\
                and delet_node.LeftChild is not None:
                new_node = self.FinMinMax(delet_node.RightChild, False)
                new_node.Parent = None
                new_node.LeftChild = delet_node.LeftChild
                delet_node.LeftChild.Parent = new_node
                self.Root = new_node
                return True

             #если удаляем левого потомка узла у которого есть только левый потомок
            elif delet_node.Parent is not None\
                and delet_node.RightChild is None\
                and delet_node.LeftChild is not None\
                and delet_node.Parent.LeftChild is delet_node:
                    delet_node.LeftChild.Parent = delet_node.Parent
                    delet_node.Parent.LeftChild = delet_node.LeftChild
                    delet_node.Parent = None
                    return True
            #если удаляем левого потомка узла у которого есть только правый потомок
            elif delet_node.Parent is not None\
                and delet_node.RightChild is not None\
                and delet_node.LeftChild is None\
                and delet_node.Parent.LeftChild is delet_node:
                    delet_node.RightChild.Parent = delet_node.Parent
                    delet_node.Parent.LeftChild = delet_node.RightChild
                    delet_node.Parent = None
                    return True
            #если удаляем правого потомка узла у которого есть только левый потомок
            elif delet_node.Parent is not None\
                and delet_node.RightChild is  None\
                and delet_node.LeftChild is not None\
                and delet_node.Parent.RightChild is delet_node:
                    delet_node.LeftChild.Parent = delet_node.Parent
                    delet_node.Parent.RightChild = delet_node.LeftChild
                    delet_node.Parent = None
                    return True
            #если удаляем правого потомка узла у которого есть только правый потомок
            elif delet_node.Parent is not None\
                and delet_node.RightChild is not None\
                and delet_node.LeftChild is None\
                and delet_node.Parent.RightChild is delet_node:
                    delet_node.RightChild.Parent = delet_node.Parent
                    delet_node.Parent.RightChild = delet_node.RightChild
                    delet_node.Parent = None
                    return True

            # 11 если удаляем левого потомка
            elif delet_node.Parent is self.Root and self.Root.LeftChild == delet_node:
                self.Root.LeftChild = None
                return True

            # 12 если удаляем правого  потомка
            elif delet_node.Parent is self.Root and self.Root.RightChild == delet_node:
                self.Root.RightChild = None
                return True

        else:
            return False # если узел не найден

    def counter(self, node, count_number) -> int:
        if self.Root == None:
            return 0
        count_number += 1
        if node.LeftChild is not None:
            count_number = self.counter(node.LeftChild, count_number)
        if node.RightChild is not None:
            count_number = self.counter(node.RightChild, count_number)
        return count_number

    def Count(self) -> int:
        return self.counter(self.Root, 0) # количество узлов в дереве
        # try:
        #     return self.counter(self.Root, 0) # количество узлов в дереве
        # except:
        #     return 0

# node = BSTNode(20,random.randint(0,50),None)
# tree = BST(node)
# # недобавляетпочему-торавные ключи
# for i in range(20):
#     tree.AddKeyValue(i,5)
# for j in range(20):
#     tree.DeleteNodeByKey(j)
#     print(tree.Count())
#     print("итер №----------------",j)


# # tree.AddKeyValue(16,5)
# # tree.AddKeyValue(13,5)
# # tree.DeleteNodeByKey(13)
# # tree.DeleteNodeByKey(14)
# # print(tree.Count())