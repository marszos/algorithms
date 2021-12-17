def insertion_sort(arr):
    
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1 
        
        arr[j+1] = key 
    
    return arr
  
  arr = [100,10, 1, -1, 0, 7, -10]
  insertion_sort(arr)
