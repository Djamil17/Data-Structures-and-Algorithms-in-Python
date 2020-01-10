
"""
Script:Linear_Structures.py
Description: Description, explanation of Linear Structures 
Author: Djamil Lakhdar-Hamina, Carlos Perez 

Contents: 
1. Linear Structures and ADT 
2. Stack, description, implentation 
3. Queue, description, implentation 
4. Linked list, description ,implentation 
5. Doubly linked List, description ,implentation 
6. Circular Linked List
7. Sparse Matrix Conversion using Linked List 
"""


## Stack:

## A stack is an adt which follows LIFO and supports the following methods 
## 1. push 2.pop 3. peek 4. size

class Stack():
   def __init__(self):
      self.items=[]
  
   def push(self,item):
      self.items.append(item)
    
   def pop(self):
      self.items.pop()
      
   def peek(self):
     return self.items[-1]
     
   def size(self):
      return len(self.items)
   
## Queue:

## A queue is an adt which follows FIFO and supports the following methods 
## 1. enqueue 2. dequeu 3. size

class Queue():
   def __init__(self):
      self.items=[]
      
   def enqueue(self, item):
      self.items.insert(0,item)
      
   def dequeue(self):
      self.items.pop()
      
   def size(self):
      return len(self.items) 

## Dequeue:

 class Deque():
   def __init__(self):
      self.items=[]

    def addFront(self):
      self.items.append(item) 
   
    def addRear(self, item):
      self.items.insert(0, item) 
    
    def removeFront(self):
       return self.items.pop()
       
     def removeRear(self):
       return self.items.pop(0)
  
   def size(self):
      return len(self.items) 
   
## Linked List:
class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data=newdata

    def setNext(self, newnext):
        self.next=newnext
         
    def __repr__(self):
        return f'{self.data},{self.next}'  
      
class List:
    def __init__(self,initdata):
        n=Node()
        n.setData(initdata)
        self.head = n

    def add(self, item):
        a=Node()
        a.setData(item)
        temp = a
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current is not None:
            current = current.getNext()
            count = count + 1
        return count

    def search(self, item):
        current = self.head
        found = False
        while current.getData() != item and not found:
            if current == item:
                found = True
            else:
                current = current.getNext()
        return current, found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        ## remove head
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
     
     def __repr__(self):
        return f'{self.head}'

  ## doubly linked list 

class Node(object):

def __init__(self, data, prev, next):
self.data = data
self.prev = prev
self.next = next

class DoubleLL(object):

head = None
tail = None

def insert(self, item):

new_object = Node(data = item)

new_object.next = self.head
new_object.prev = None

if self.head is not None:
self.head.prev = new_object

self.head = new_object

class dNode: 
    def __init__(self, initdata):
        self.data=initdata 
        self.next=None
        self.previous=None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
   
    def getPrevious(self)
        return self.previous
   
    def setData(self,newdata):
        return self.initdata=newdata 
   
    def setNext(self,newnext):
        return self.next=newnext 
   
    def setPrevious(self, newprev):
        return self.previous=newprev 
   
class doublelinkedList(dNode):
      def __init__(self):
        self.head=None
    
      def add(self,item):
        temp=Node(item)
        temp.setNext(self.head)
        self.head=temp 
    
      def length(self):
        current=self.head
        count=0
        while current != None: 
            current=current.getNext()
            count+=1

      def search(self, item):
        current=self.head
        found=False
        while current != item and not found:   
            if current.getNext() == item:
                found=True
            else:
                current= current.getNext()

        return current, found  

    def remove(self, item):
        current=self.head
        previous= current.getPrevious()
        found= False
        while current != None and not found: 
            if current.getNext()==item:
                found=True
            else: 
                previous=current
                current=current.getNext()

        ## remove head 
        if previous == None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())
            previous.setPrevious(current.getPrevious())
            
class CircularList:
     def __init__(self, initdata,initdata2):
          n = Node()
          n.setData(initdata)
          self.head = n
          n2= Node()
          n2.setData(initdata2)
          self.tail=n2 
          self.head.setNext(self.tail)
          self.tail.setNext(self.head)

     def add(self, item):
          a = Node()
          a.setData(item)
          temp = a
          temp.setNext(self.head)
          self.head = temp

     def length(self):
          current = self.head
          count = 0
          while current is not None:
               current = current.getNext()
               count = count + 1
          return count

     def search(self, item):
          current = self.head
          found = False
          while current.getData() != item and not found:
               if current == item:
                    found = True
               else:
                    current = current.getNext()
          return current, found

     def remove(self, item):
          current = self.head
          previous = None
          found = False
          while current is not None and not found:
               if current.getData() == item:
                    found = True
               else:
                    previous = current
                    current = current.getNext()

          ## remove head
          if previous is None:
               self.head = current.getNext()
          else:
               previous.setNext(current.getNext())

     def __repr__(self):
          return f'{self.head}'
            
## region: dna 
## We will use two linked lists to represent 
## TODO: Just use a node for a single pair, no extra pair Node 

class NucleoTide:
    nucleobase_kind = ['A', 'T', 'C', 'G']
    phosphate='p'
    deoxyribose='d'

    def __init__(self):
        self.nucleotide=None
        self.nextnucleotide=None
        self.left_backbone=self.phosphate + '-'  + self.deoxyribose
        self.right_backbone=self.deoxyribose + '-' + self.phosphate


    def autosetBase(self):
        self.nucleotide=random.sample(self.nucleobase_kind,1)[0]

    def manualsetBase(self, item):
        self.nucleotide=item

    def autosetNext(self):
        self.nextnucleotide=random.sample(self.nucleobase_kind,1)[0]

    def setNext(self,item):
        self.nextnucleotide = item

    def getBase(self):
        return self.nucleotide

    def getNext(self):
        return self.nextnucleotide

    def display(self):
        print(self.left_backbone  +'-' + self.nucleotide + self.nucleotide + '-' + self.right_backbone)


class DNA(NucleoTide):

    def pair_nitrogeneous_base(self,item):
        temp=''
        if item == 'A':
            temp = 'T'
        elif self.nucleotide == 'C':
            temp = 'G'
        elif self.nucleotide == 'T':
            temp = 'A'
        elif self.nucleotide == 'G':
            temp = 'C'

        return temp

    def __init__(self):
        base = NucleoTide()
        pair_base = NucleoTide()
        base.autosetBase()
        self.head = base
        pair_base.manualsetBase(self.pair_nitrogeneous_base(self.head.getBase()))
        self.pair = pair_base
        self.tail=None


    def assembleGenome(self, length):
        assembled = False
        counter = 0
        while counter > length and not assembled:
            base = NucleoTide()
            pair_base = NucleoTide()
            base.setNext(self.head )
            base.setNext(self.head )
            pair_base.setNext(self.pair)
            self.head=base
            self.pair=pair_base

            counter += 1
## endregion 

## region: using linked list for sparse matrix : https://www.geeksforgeeks.org/sparse-matrix-representation/
class compactMatrixNode:
    def __init__(self):
        self.data = None
        self.row = None
        self.column = None
        self.next = None

    def getData(self):
        return self.data

    def getRow(self):
        return self.row

    def getColumn(self):
        return self.column

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setRow(self, rownum):
        self.row = rownum

    def setColumn(self, columnnum):
        self.column = columnnum

    def setNext(self, newnext):
        self.next = newnext

    def __repr__(self):
        return f'{self.data},{self.row},{self.column},{self.next}'


class compactMatrixLinkedList:
    def __init__(self):
        self.head = None

    def add(self, item, row, column):
        if self.head is None:
            n = compactMatrixNode()
            n.setData(item)
            n.setRow(row)
            n.setColumn(column)
            self.head=n
        else:
            self._add(item, row, column)

    def _add(self, item,row,column):
       node = compactMatrixNode()
       node.setData(item)
       node.setNext(self.head)
       node.setRow(row)
       node.setColumn(column)
       self.head = node


    def __repr__(self):
        return f'{self.head}'


def convertSparsetoCompact(nested_list):
    compactMatrix = compactMatrixLinkedList()
    for row in range(len(nested_list[0:])):
        for column in range(len(nested_list[row:][0])):
            if nested_list[row][column] != 0:
                print('Storing {} in row {} and column {}'.format(nested_list[row][column], row, column))
                compactMatrix.add(nested_list[row][column], row, column)
                  
    return compactMatrix

##endregion:**************
                   
## region: 
if __name__ == '__main__': 
   main():
## endregion                  
