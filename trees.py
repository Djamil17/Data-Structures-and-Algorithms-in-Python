"""
Title: Binary Tree
Author: Djamil Lakhdar-Hamina
Date: 07/11/2019
"""

"""
Analysis of NCA-algorithm


"""


## Read in data
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
            print('No value')
        else:
            self._find(item, self.root)

    def _find(self,item ,node):
        found=False
        if node.data == item:
            found=True
        elif node.data < item:
            if node.left==item:
                found=True
            else:
                self._find(item, node.left)
        elif node.data > item:
            if node.right==item:
                found=True
            else:
                self._find(item,node.right)

        return found

    def PrintTree(self):
        if self.root is not None:
            self._PrintTree(self.root)

    def _PrintTree(self, node):
        if node is not None:
            self._PrintTree(node.left)
            print(str(node.data))
            self._PrintTree(node.right)


## Count edges to target
b=BinaryTree()
b.add(2)
b.add(3)
b.add(5)
b.PrintTree()
print(b.find(5))

