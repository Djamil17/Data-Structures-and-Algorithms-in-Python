"""
Title: Tree Data-Structure 
Author: Djamil Lakhdar-Hamina
Date: 07/11/2019
"""


## List of list style
class BinaryTree:
    def __init__(self, r):
        self.root = [r, [], []]

    def insertLeft(self, newbranch):
        temp = self.root.pop(1)
        if len(temp) > 1:
            self.root.insert(1, [newbranch, temp, []])
        else:
            self.root.insert(1, [newbranch, [], []])

    def insertRight(self, newbranch):
        temp = self.root.pop(2)
        if len(temp) > 1:
            self.root.insert(2, [newbranch, temp, []])
        else:
            self.root.insert(2, [newbranch, [], []])

    def getRootNode(self):
        return self.root[0]

    def getLeftChild(self):
        return self.root[1]

    def getRightChild(self):
        return self.root[2]

    def __str__(self):
        return self.root.__str__()

    ## region : always 0 at front


class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[i // 2]
                self.heapList[i // 2] = temp
        i //= 2

    def insert(self, k):
        self.heapList.append(k)
        self.current_size = self.current_size + 1
        self.percUp(self.current_size)

    def percDown(self, i):
        while i * 2 <= self.current_size:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc

    def delChild(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList
        self.heapList.pop(1)
        self.percDown(1)
        return retval

    def minChild(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return self.heapList[i * 2]
            else:
                return self.heapList[i * 2 + 1]

            ## endregion : ****************


## Node and reference style
class BinarySearchTree:

    def __init__(self, item):
        self.root = item
        self.left = None
        self.right = None

    def setRoot(self, newval):
        self.root = newval

    def setRightChild(self, item):
        self.right = item

    def setLeftChild(self, item):
        self.item = item

    def getRootValue(self):
        return self.root

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def insertLeft(self, item):
        if self.left is None:
            self.left = BinaryTree(item)
        else:
            temp = BinaryTree(item)
            temp.left = self.left
            self.left = temp

    def insertRight(self, item):
        if self.right is None:
            self.right = BinaryTree(item)
        else:
            temp = BinaryTree(item)
            temp.right = self.right
            self.right = temp

    def preorder(self):
        print(self.root)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.postorder()
        print(self.root)
        if self.right:
            self.right.postorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.root)


## endregion:************                        

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:

    def __init__(self):
        self.root = None

    def add(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            self._add(item, self.root)

    def _add(self, val, node):
        if node.data < val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._add(val, node.left)
        elif node.data > val:
            if node.right is None:
                node.right = Node(val)
            else:
                self._add(val, node.left)

    def find(self, item):
        if self.root is None:
            return None
        else:
            return self._find(item, self.root)

    def _find(self, val, node):
        if node.data == val:
            return val
        elif node.data < val:
            if node.left == val:
                return val
            else:
                self._find(val, node.left)
        elif node.data > val:
            if node.right == val:
                return val
            else:
                self._find(val, node.right)

        return val

    def PrintTree(self):
        if self.root is not None:
            self._PrintTree(self.root)

    def _PrintTree(self, node):
        if node is not None:
            self._PrintTree(node.left)
            print(str(node.data))
            self._PrintTree(node.right)


class TreeNode:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def Length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        self.root.__iter__()

class BinarySearchTree:
    def __init__(self, key, val, parent, left, right):
        self.key = key
        self.payload = val
        self.parent = parent
        self.leftchild = left
        self.rightchild = right

    def hasRightChild(self):
        return self.rightchild

    def hasLeftChild(self):
        return self.leftchild

    def isLeftchild(self):
        return self.parent.leftchild == self

    def isRightchild(self):
        return self.parent.rightchild == self

    def hasChild(self):
        return self.leftchild or self.rightchild

    def hasBothChild(self):
        return self.leftchild and self.rightchild

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightchild or self.leftchild)

    def replaceNode(self, key, payload, lc, rc):
        self.key = key
        self.payload = payload
        self.rightchild = rc
        self.leftchild = lc
        if self.hasLeftChild():
            self.leftchild.parent = self
        if self.hasRightChild():
            self.rightchild.parent = self

    def add(self, key, payload):
        if self.root:
            self._add(key, payload, self.root)
        else:
            self.root = BinarySearchTree(key, payload)

        self.size += 1

    def _add(self, key, val, node):
        if key < node.key:
            if node.hasLeftChild():
                self._add(key, val, node.leftchild)
            else:
                node.leftchild = BinarySearchTree(key, val, parent=node)
        else:
            if node.hasrightChild():
                self.add(key, val)
            else:
                node.rightchild = BinarySearchTree(key, val, parent=node)

    def get(self, key):
        if self.root:
            res = self._get(self.root, key)
            return res.payload
        else:
            return None

    def _get(self, currentnode, key):
        if currentnode.key == key:
            return currentnode
        elif currentnode.key > key:
            return self._get(currentnode.rightchild, key)
        elif currentnode.key < key:
            return self._get(currentnode.rightchild, key)
        else:
            return None

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        if self.get(item):
            return True
        else:
            return False

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftchild():
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightchild():
                    yield elem

    def delete(self, key):
        if self.size > 1:
            res = self.get(key)
            if res:
                self.remove(res)
                self.size -= 1
            else:
                raise KeyError("Key {} does not exist".format(key))
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Key {} does not exist".format(key))

    def remove(currentnode):
        if currentnode.isLeaf():
            if currentnode.isRightchild():
                currentnode.parent.leftchild = None
            elif currentnode.isLeftchild():
                currentnode.parent.rightchild = None
        elif currentnode.hasBothChild():
            suc=currentnode.sucessor()
            suc.spliceOut(suc)
            currentnode.key=suc.key
            currentnode.payload=suc.key
        elif currentnode.hasChild():
            if currentnode.isLeftchild():
                if currentnode.hasLeftChild():
                    currentnode.parent.leftchild = currentnode.leftchild
                    currentnode.leftchild.parent = currentnode.parent
                elif currentnode.hasRightChild():
                    currentnode.parent.rightchild = currentnode.rightchild
                    currentnode.rightchild.parent = currentnode.parent
            elif currentnode.isRightchild():
                if currentnode.hasLeftChild():
                    currentnode.parent.leftchild = currentnode.leftchild
                    currentnode.leftchild.parent = currentnode.parent
                elif currentnode.hasRightChild():
                    currentnode.parent.rightchild = currentnode.rightchild
                    currentnode.rightchild.parent = currentnode.parent
            elif currentnode.isRoot():
                if currentnode.hasLeftChild():
                    currentnode.replaceNode(currentnode.leftchild.key,
                                            currentnode.leftchild.payload,
                                            lc=currentnode.leftchild.leftchild,
                                            rc=currentnode.leftchild.rightchild)

                else:
                    currentnode.replaceNode(currentnode.leftchild.key,
                                            currentnode.leftchild.payload,
                                            lc=currentnode.rightchild.leftchild,
                                            rc=currentnode.rightchild.rightchild)

    def sucessor(currentnode):
        suc=None
        if suc.hasRightChild():
            suc.rightchild.findMin()
        return suc 

    def findMin(currentnode):
        current=currentnode
        while currentnode.hasLeftchild():
            current= currentnode.leftchild
        return current
    
    def spliceOut(currentnode):
        if currentnode.isLeaf():
            if currentnode.isLeftChild():
                currentnode.parent.leftchild=None
            else: 
                currentnode.parent.rightchild=None
        elif currentnode.hasChild():
           if currentnode.hasLeftChild():
              if currentnode.isLeftChild():
                 currentnode.parent.leftchild=currentnode.leftchild 
              else: 
                 currentnode.parent.rightchild=currentnode.leftchild 
                 currentnode.rightchild.parent=currentnode.parent
           else:
              if currentnode.hasRightChild():
                 if currentnode.isLeftChild():
                    currentnode.parent.leftchild=currentnode.rightchild
                 else:
                    currentnode.parent.rightchild=currentnode.rightchild 
                    currentnode.rightchild.parent=currentnode.parent
                
    def __del__(self, key):
        self.delete(key)
