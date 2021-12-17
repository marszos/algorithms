def heapify(arr,n,i):
    largest = i 
    
    l = 2 * i + 1
    r = 2 * i + 2 
    
    if l < n and arr[largest] < arr[l]:
        largest = l 
        
    if r < n and arr[largest] < arr[r]:
        largest = r 
    
    
    if largest!= i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr,n,largest)
        
def heapSort(arr):
    n = len(arr)
    
    for i in range(n // 2, -1 , -1):
        heapify(arr,n,i)
        
    for i in range(n-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr,i,0)
    
    return arr

 arr = [3, 1, -1, 0, 2, 5,6,4]
 heapSort(arr)
