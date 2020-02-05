"""
Script:searching_and_sorting_algorithms.py
Description: Description, explanation of famous sorting and searching algorithms
Author: Djamil Lakhdar-Hamina, Carlos Perez 
Contents: TODO  
"""

import time 
import numbers
## sequential search of list 

def seqScan(alist, item):
   found=False
   pos=0
   while pos < len(alist) and not found:
        if alist[pos] == item:
            found=True
        else: 
            pos+=1 
            
def binarySearch(alist, item):
    found=False
    first=0
    last=len(alist)-1
    while first <= last and not found:
        mid=(first+last)//2
        if alist[mid] == item:
            found=True
        else :
            if item < alist[mid]:
                last=mid-1
            else:
                first=mid+1

    return found

def binarySearch(alist, item):
    found=False
    midpoint=len(alist)//2
    if midpoint == item:
        found=True
    else:
        if alist[midpoint] > item :
            binarySearch(alist[:midpoint],item)
        else: 
            binarySearch(alist[midpoint+1:],item)
    return found 

## hash table

class HashTable:
    def __init__(self, size):
        self.size = size
        if not isinstance(self.size, numbers.Integral):
            raise TypeError('Size of slots must be a prime number')
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __str__(self):
        print(self.size)
        print(self.slots)
        print(self.data)

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))
        print(hashvalue)
        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, self.size)
                while nextslot != None and self.slots[nextslot] != key:
                      nextslot = self.rehash(hashvalue, len(self.slots))


                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data

    def hashfunction(self, key, size):
        return key%size

    def rehash(self, oldhash, size):
        return (oldhash + 1)%size

    def get(self, key):
        startslot=self.hashfunction(key, self.size)
        data = None
        found = False
        stop= False
        position=startslot
        while position is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
               position=self.rehash(key, size.self)
               if position=startslot:
                  stop=True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        return self.put(key, data)

## bubble sort 
start_time = time.time()

def bubble_sort(alist):
    for num in range(len(alist)-1,0, -1):
        for i in range(num):
            if alist[i] > alist[i+1]:
                temp=alist[i]
                alist[i]=alist[i+1]
                alist[i+1]=temp
    return alist 

start_time2 = time.time()

## bubble sort , version 2 with simultaneous assignment 
def bubble_sort2(alist):
    for num in range(len(alist)-1,0, -1):
        for i in range(num):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
    return alist 

## selection sort 
def selectionSort(alist):
    for fillslot in range(len(alist)-1,0, -1):
        maxposition=0
        for location in range(1, fillslot+1):
            if alist[location] > alist[maxposition]:
                print(alist[location], alist[maxposition])
                maxposition= location

        alist[fillslot], alist[maxposition]= alist[maxposition], alist[fillslot]

    return alist

def select(alist):
    maxposition=0
    for idx in range(len(alist)-1,0,1):
        if alist[idx] > alist[maxposition]:
            maxposition=idx

    return maxposition

def selectsort(alist):
    for position in range(len(alist)-1, 0 ,-1):
        maxposition=select(alist[position:])
        alist[position], alist[maxposition]= alist[maxposition], alist[position]

    return alist

## region: mergesort

def mergesort(alist):
    if len(alist) > 1: 
         
        print('Splitting:{}'.format(alist))
      
        midpoint=len(alist)//2
        left=alist[:midpoint]
        right=alist[midpoint:]
    
        mergesort(left)
        mergesort(right)
        
        i=j=k=0
    
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                alist[k]=left[i]
                i +=1
                k+=1
            else:
                alist[k]=right[j]
                j +=1
                k+=1
                
    
        print('Merging:{}'.format(alist))
        
        while i < len(left):
            alist[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            alist[k]=right[j]
            j=j+1
            k=k+1
    
    return f'The merged list is : {alist}'
   
##endregion: *************
## region: quicksort

def quickSort(alist,first, last):
    quickSortHelper(alist, 0 ,len(alist)-1)
    return alist

def quickSortHelper(alist, first,last):
    if first<last:

        splitpoint=partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist,splitpoint+1, last)

def partition(alist, first, last):
    pivotvalue=alist[first]
    leftmark=first + 1
    rightmark=last

    done=False

    while not done :
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark +=1
        while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
            rightmark -=1
        if rightmark < leftmark:
            done=True
        else:
            alist[leftmark],alist[rightmark]=alist[rightmark],alist[leftmark]

    alist[first] ,alist[rightmark]= alist[rightmark], alist[first]

    return rightmark
   
##endregion: ***********

## endregion 
