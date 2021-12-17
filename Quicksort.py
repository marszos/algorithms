def qs(arr,l,r):
    if l >= r:
        return 
    
    p = partition(arr,l,r)
    qs(arr,l,p-1)
    qs(arr,p+1,r)
    
    return arr



def partition(arr,l,r):
    pivot = arr[r]
    j = l - 1
    
    for i in range(l,r):
        if arr[i] < pivot:
            j += 1 
            arr[j], arr[i] = arr[i], arr[j]
    
    arr[r], arr[j+1] = arr[j+1], arr[r]
    
    return j+1
  
  arr = [3, 1, -1, 0, 2, 5,6,4]
  qs(arr,0,len(arr)-1)
