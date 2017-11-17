
from array import array
import math

def array_index(i):
    return i-1

def parent(i):
    return int(math.floor(i/2))

def left(i):
    return 2*i

def right(i):
    return 2*i+1

def swap(A,a,b):
    a = array_index(a)
    b = array_index(b)
    tmp = A[a]
    A[a] = A[b]
    A[b] = tmp
    return
    
def max_heapify(A,i,heapSize):
    l = left(i)
    r = right(i)
    largest = i
    if(l<=heapSize) and (A[array_index(l)]>A[array_index(largest)]):
        largest = l
    if(r<=heapSize) and (A[array_index(r)]>A[array_index(largest)]):
        largest = r
    if largest != i:
        swap(A,i,largest)
        max_heapify(A, largest, heapSize)
    return

def build_max_heap(A):
    heapSize = len(A)
    last_parent = int(math.floor(len(A)/2))
    for i in reversed(range(1,last_parent+1)):
        max_heapify(A, i, heapSize)
        
def heap_sort(A):
    build_max_heap(A)
    heapSize = len(A)
    for i in reversed(range(2,len(A)+1)):
        swap(A,1,i)
        heapSize = heapSize -1
        max_heapify(A, 1, heapSize)
    
arr = array('i',[52,-100,942,0,2,23,-23,89,2,63])
print arr
heap_sort(arr)
print arr