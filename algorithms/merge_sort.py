
from array import array

def merge_sort(arr):
    N = len(arr)
    if(N==1):
        return arr
#     if(N==2):
#         if(arr[1]<arr[0]):
#             tmp = arr[1]
#             arr[1] = arr[0]
#             arr[0] = tmp
#         return arr
    
    l1 = []
    for i in range(0,int(N/2)):
        l1.append(arr[i])
    a1 = array('i',l1)
    l2 = []
    for i in range(int(N/2),N):
        l2.append(arr[i])
    a2 = array('i',l2)
    
#     print '+++ N : ' + str(N) + ' a1 : ' + str(len(a1)) + ' a2 : ' + str(len(a2))

    a1 = merge_sort(a1)
    a2 = merge_sort(a2)

    i1 = 0
    i2 = 0
    I = 0
    earlyExit = -1
    while(I<N and earlyExit==-1):
        if(a1[i1]<a2[i2]):
            arr[I] = a1[i1]
            i1 = i1+1
        else:
            arr[I] = a2[i2]
            i2 = i2+1
        I=I+1
        if(i1==len(a1)):
            earlyExit = 1
        if(i2==len(a2)):
            earlyExit = 2
    
    if(N==2):
        print a1
        print a2
        print arr
    return arr

arr = array('i',[52,-100,942,0,2,23,-23,89,2,63])
print merge_sort(arr)