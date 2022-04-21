def two_sum(nums, target):
    
    seen = {}
    
    for i, num in enumerate(nums):
        if target - num in seen:
            return ([seen[target - num], i])
        else:
            if num not in seen:
                seen[num] = i
            
         
nums1 = [3,2,4]
target1 = 6

nums = [2,7,11,15]
target = 9

