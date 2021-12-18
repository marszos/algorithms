def interpolation_search(arr,lo,hi,x):
    if lo <= hi and x <= arr[hi] and x >= arr[lo]:
        pos = int(lo + (x - arr[lo]) / (arr[hi] - arr[lo])*(hi - lo))
        
        if arr[pos] == x:
            return pos 
        elif arr[pos] > x:
            return interpolation_search(arr,lo, pos-1, x)
        else:
            return interpolation_search(arr,pos+1,hi, x)
    else: 
        return -1 
      
      
      
arr = [2, 3, 4, 10, 40]
x = 10

interpolation_search(arr,0, len(arr)-1, x)
