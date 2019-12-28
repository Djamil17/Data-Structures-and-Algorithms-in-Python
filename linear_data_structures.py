
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
      
   def size(self)
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
       
     def removeRear(self)
       return self.items.pop(0)
  
   def size(self)
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
