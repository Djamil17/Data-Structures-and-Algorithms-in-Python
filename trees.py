"""
Title: Binary Tree
Author: Djamil Lakhdar-Hamina
Date: 07/11/2019
"""

## List of list style 

class BinaryTree:
    def __init__(self, r):
        self.root= [r, [], []]


    def insertLeft(self, newbranch):
        temp=self.root.pop(1)
        if len(temp) > 1 :
            self.root.insert(1, [newbranch, temp, []])
        else:
            self.root.insert(1, [newbranch, [], []])

    def insertRight(self, newbranch):
        temp=self.root.pop(2)
        if len(temp) > 1 :
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
                                         
## Node and reference style
class BinarySearchTree:

    def __init__(self, item):
        self.root = item
        self.left = None
        self.right = None

    def setRoot(self,newval):
        self.root=newval

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

    def insertLeft(self,item):
        if self.left is None:
            self.left=BinaryTree(item)
        else:
            temp=BinaryTree(item)
            temp.left=self.left
            self.left=temp

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
        self.root=None

    def add(self,item):
        if self.root is None:
            self.root=Node(item)
        else:
            self._add(item,self.root)

    def _add(self, val, node):
        if node.data < val:
            if node.left is None:
                node.left=Node(val)
            else:
                self._add(val, node.left)
        elif node.data > val:
            if node.right is None:
                node.right=Node(val)
            else:
                self._add(val,node.left)

    def find(self,item):
        if self.root is None:
            return None
        else:
            return self._find(item, self.root)

    def _find(self,val ,node):
        if node.data == val:
            return val
        elif node.data < val:
            if node.left==val :
                return val
            else:
                self._find(val, node.left)
        elif node.data > val:
            if node.right==val:
                return val
            else:
                self._find(val,node.right)

        return val
    
    def PrintTree(self):
        if self.root is not None:
            self._PrintTree(self.root)

    def _PrintTree(self, node):
        if node is not None:
            self._PrintTree(node.left)
            print(str(node.data))
            self._PrintTree(node.right)

            
## main 
def main():
    
## Count edges to target
if __name__=='__main__': 
   main()
