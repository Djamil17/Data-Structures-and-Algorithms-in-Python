
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

## Queue:

## Dequeue:

## Linked List:

class Node: 
   
    def __init__(self, initdata):
        self.data=initdata 
        self.next=None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.head
    def setData(self,newdata):
        return self.initdata=newdata 
    def setNext(self,newnext):
        return self.next=newnext 

class List(Node):
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
        previous= None
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
            
  ## doubly linked list 
