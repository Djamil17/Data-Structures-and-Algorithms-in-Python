"""
Title: Binary Tree
Author: Djamil Lakhdar-Hamina
Date: 07/11/2019
"""

"""

"""
## List of list style 

def BinaryTree(r):
    return [r, [], []]

def insertLeft(root, newbranch):
    temp=root.pop(1)
    if len(temp) > 1 : 
        root.insert(1, [newbrach, temp, [])
    else:
        root.insert(1, [newbrach, [], [])
                        
def insertRight(root, newbranch):
    temp=root.pop(2)
    if len(temp) > 1 : 
        root.insert(2, [newbrach, temp, [])
    else:
        root.insert(2, [newbrach, [], [])


## Node and reference style
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


## Count edges to target
if __name__=='main()': 
main():
b=BinaryTree()
b.add(2)
b.add(3)
b.add(5)
b.PrintTree()
