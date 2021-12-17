def bubble_sort(arr):
    
    for i in range(len(arr)):
        for j in range(0,len(arr)-1-i):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    
    return arr
