import random
class BSTNode:

    def __init__(self, key, val, parent):
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


    def FindByKey_node(self, key, node):
        if key == node.NodeKey:
            return [node, False, False]

        if node.LeftChild is not None and key < node.NodeKey:
            return self.FindByKey_node(key, node.LeftChild)

        elif node.RightChild is not None and key > node.NodeKey:
            return self.FindByKey_node(key, node.RightChild)

        elif node.LeftChild is None and key < node.NodeKey:
            return [node, True, True]

        elif node.RightChild is None and key > node.NodeKey:
            return [node, False, False]

        elif node.Parent is None and node.LeftChild is None and node.RightChild is None :
                return[node,None,False]




    def FindNodeByKey(self, key):
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
        return find_node_list

    def init_new_node(self, new_key, new_val, new_parent, ToLeft):
        new_node = BSTNode(new_key, new_val, new_parent)
        if ToLeft == True:
            new_parent.LeftChild = new_node
        else:
            new_parent.RightChild = new_node


    def AddKeyValue(self, key, val):
        # добавляем ключ-значение в дерево
        find_node_list = self.FindNodeByKey(key)
        if find_node_list[1] == False:
            self.init_new_node(key, val, find_node_list[0], find_node_list[2])

        if find_node_list[1] == True:
            self.init_new_node(key, val, find_node_list[0], find_node_list[2]) # если ключ уже есть

    def FinMinMax(self, FromNode, FindMax):
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

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        delet_node = self.FindNodeByKey(key)
        if delet_node[1] == True or delet_node[1] == False:
            delet_node = delet_node[0]

            # если удаляем правый подкорень и есть только правый потомок
            if delet_node.Parent is not None \
                and delet_node.RightChild is not None \
                and delet_node.LeftChild is None\
                and delet_node.Parent.LeftChild is None: # правый подкорень
                delet_node.Parent.RightChild = delet_node.RightChild
                delet_node.RightChild.Parent = delet_node.Parent

            # если удаляем левый подкорень и есть только правый потомок
            elif delet_node.Parent is not None \
                and delet_node.RightChild is not None \
                and delet_node.LeftChild is None\
                and delet_node.Parent.RightChild is None: # левый подкорень
                delet_node.Parent.LeftChild = delet_node.RightChild
                delet_node.RightChild.Parent = delet_node.Parent

            elif delet_node.Parent is not None \
                and delet_node.RightChild is not None \
                and delet_node.LeftChild is None\
                and delet_node.Parent.RightChild is None: # левый подкорень
                delet_node.Parent.LeftChild = delet_node.RightChild
                delet_node.RightChild.Parent = delet_node.Parent

            # если удаляем правый подкорень и есть только левый потомок
            elif delet_node.Parent is not None\
                and delet_node.RightChild is None \
                and delet_node.LeftChild is not None\
                and delet_node.Parent.LeftChild is None: # правый подкорень
                delet_node.Parent.RightChild = delet_node.LeftChild
                delet_node.LeftChild.Parent = delet_node.Parent

            # если удаляем левый подкорень и есть только левый потомок
            elif delet_node.Parent is not None\
                and delet_node.RightChild is None\
                and delet_node.LeftChild is not None\
                and delet_node.Parent.RightChild is None: # левый подкорень
                delet_node.Parent.LeftChild = delet_node.LeftChild
                delet_node.LeftChild.Parent = delet_node.Parent


            # если удаляем единственный! корень и есть только правый потомок
            elif delet_node.Parent is None\
                and delet_node.RightChild is not None\
                and delet_node.LeftChild is None:
                self.Root = delet_node.RightChild
                delet_node.RightChild.Parent = None

            # если удаляем единственный!корень и есть только левый потомок
            elif delet_node.Parent is None\
                and delet_node.RightChild is None\
                and delet_node.LeftChild is not None:
                self.Root = delet_node.LeftChild
                delet_node.LeftChild.Parent = None

            elif delet_node.Parent is not None\
                and delet_node.RightChild is None\
                and delet_node.LeftChild is None\
                and delet_node.Parent.LeftChild == delet_node:
                    delet_node.Parent.LeftChild = None

            elif delet_node.Parent is not None\
                and delet_node.RightChild is None\
                and delet_node.LeftChild is None\
                and delet_node.Parent.RightChild == delet_node:
                    delet_node.Parent.RightChild = None


            # если удаляем корень и нет потомков
            elif delet_node.Parent is None \
                and delet_node.RightChild is None \
                and delet_node.LeftChild is None:
                self.Root = None


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


            # 10  если удаляем корень и есть оба потомка
            elif delet_node.Parent is None\
                and delet_node.RightChild is not None\
                and delet_node.LeftChild is not None:
                new_node = self.FinMinMax(delet_node.RightChild, False)
                new_node.Parent = None
                new_node.LeftChild = delet_node.LeftChild
                delet_node.LeftChild.Parent = new_node
                self.Root = new_node

             #если удаляем левого потомка узла у которого есть только левый потомок
            elif delet_node.Parent is not None\
                and delet_node.RightChild is None\
                and delet_node.LeftChild is not None\
                and delet_node.Parent.LeftChild is delet_node:
                    delet_node.LeftChild.Parent = delet_node.Parent
                    delet_node.Parent.LeftChild = delet_node.LeftChild
                    delet_node.Parent = None
            #если удаляем левого потомка узла у которого есть только правый потомок
            elif delet_node.Parent is not None\
                and delet_node.RightChild is not None\
                and delet_node.LeftChild is None\
                and delet_node.Parent.LeftChild is delet_node:
                    delet_node.RightChild.Parent = delet_node.Parent
                    delet_node.Parent.LeftChild = delet_node.RightChild
                    delet_node.Parent = None
            #если удаляем правого потомка узла у которого есть только левый потомок
            elif delet_node.Parent is not None\
                and delet_node.RightChild is  None\
                and delet_node.LeftChild is not None\
                and delet_node.Parent.RightChild is delet_node:
                    delet_node.LeftChild.Parent = delet_node.Parent
                    delet_node.Parent.RightChild = delet_node.LeftChild
                    delet_node.Parent = None
            #если удаляем правого потомка узла у которого есть только правый потомок
            elif delet_node.Parent is not None\
                and delet_node.RightChild is not None\
                and delet_node.LeftChild is None\
                and delet_node.Parent.RightChild is delet_node:
                    delet_node.RightChild.Parent = delet_node.Parent
                    delet_node.Parent.RightChild = delet_node.RightChild
                    delet_node.Parent = None

            # 11 если удаляем левого потомка
            elif delet_node.Parent is self.Root and self.Root.LeftChild == delet_node:
                self.Root.LeftChild = None

            # 12 если удаляем правого  потомка
            elif delet_node.Parent is self.Root and self.Root.RightChild == delet_node:
                self.Root.RightChild = None

        else:
            return False # если узел не найден

    def counter(self, node, count_number):
        count_number += 1
        if node.LeftChild is not None:
            count_number = self.counter(node.LeftChild, count_number)
        if node.RightChild is not None:
            count_number = self.counter(node.RightChild, count_number)
        return count_number

    def Count(self):
        try:
            return self.counter(self.Root, 0) # количество узлов в дереве
        except:
            return 0

# node = BSTNode(20,random.randint(0,50),None)
# tree = BST(node)
# # tree.DeleteNodeByKey(20)
# # print(tree.Count())
# tree.AddKeyValue(10,50)
# tree.AddKeyValue(28,55)
# tree.AddKeyValue(8,30)
# tree.AddKeyValue(11,30)
# tree.AddKeyValue(7,30)
# tree.AddKeyValue(26,30)
# tree.AddKeyValue(29,30)
# tree.DeleteNodeByKey(28)
# tree.AddKeyValue(random.randint(0,50),random.randint(0,50))
# tree.AddKeyValue(random.randint(0,50),random.randint(0,50))
# tree.AddKeyValue(random.randint(0,50),random.randint(0,50))
# tree.AddKeyValue(random.randint(0,50),random.randint(0,50))
# tree.AddKeyValue(random.randint(0,50),random.randint(0,50))
# tree.AddKeyValue(random.randint(0,50),random.randint(0,50))
# tree.AddKeyValue(random.randint(0,50),random.randint(0,50))
# tree.DeleteNodeByKey(random.randint(0,50))
# tree.DeleteNodeByKey(random.randint(0,50))
# tree.DeleteNodeByKey(random.randint(0,50))
# tree.DeleteNodeByKey(random.randint(0,50))
# tree.DeleteNodeByKey(random.randint(0,50))
# tree.DeleteNodeByKey(random.randint(0,50))
# print(tree.Count())