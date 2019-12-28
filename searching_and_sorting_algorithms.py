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
    last=len(alist -1) 
    while first <= last and not Found:
        mid=(first+last)//2
        if alist[mid] == item
            found=True
        else :
            if item > alist[mid]:
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
        if midpoint > item :
            binarySearch(alist[:midpoint],item)
        else midpoint < item: 
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

alist=[1,66,77,33333,5,67,2]
selectionSort(alist)
print(alist)


print("--- %s seconds ---" % (time.time() - start_time))
print("--- %s seconds ---" % (time.time() - start_time2))



if __name__ == '__main__': 
   
   

