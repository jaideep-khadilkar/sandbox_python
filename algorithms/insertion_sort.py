
from array import array
    
def insertion_sort(arr):
    for key_index,key in enumerate(arr):
        slide_index = key_index-1
        while slide_index>-1 and key<arr[slide_index]:
            arr[slide_index+1] = arr[slide_index]
            slide_index = slide_index -1
        arr[slide_index+1] = key
    print arr

arr = array('i',[52,-100,942,0,2,23,-23,89,2,63])
print arr
insertion_sort(arr)