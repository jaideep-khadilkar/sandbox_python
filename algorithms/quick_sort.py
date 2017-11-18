
from array import array

def swap(A,a,b):
    a = a-1
    b = b-1
    tmp = A[a]
    A[a] = A[b]
    A[b] = tmp
    return

def quick_sort(A,p,r):
    if(p<r):
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

def partition(A,p,r):
    x = A[r-1]
    i = p-1
    for j in range(p,r+1):
        if(A[j-1]<=x):
            i = i+1
            swap(A, i, j)
    return i

arr = array('i',[52,-100,942,0,2,23,-23,89,2,63])
print arr
quick_sort(arr,1,len(arr))
print arr
