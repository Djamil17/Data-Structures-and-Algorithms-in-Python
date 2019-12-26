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


def main():
    alist=[1,6,77,8,3,4,5,6,7,4,5,6,67]
    alist2=[1,6,77,8,3,4,5,6,7,4,5,6,67]
    bubble_sort(alist)
    bubble_sort2(alist2)
    print(alist)
    print(alist2)

print("--- %s seconds ---" % (time.time() - start_time))
print("--- %s seconds ---" % (time.time() - start_time2))
