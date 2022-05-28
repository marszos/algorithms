def how_many(nums):
    sorted_nums = sorted(nums, reverse=True)
    slownik = {}
    
    for i in range(len(sorted_nums) - 1):
        cur_num = sorted_nums[i]
        next_num = sorted_nums[i+1]
        
        if next_num < cur_num:
            slownik[cur_num] = len(sorted_nums) - (i+1)
        slownik[sorted_nums[-1]] = 0 
    
    return [slownik[k] for k in nums]
  
 
nums = [8,1,2,2,3]

# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/
