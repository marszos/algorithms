def max_number_of_coins(piles):
    sorted_piles = sorted(piles)
    end_idx = len(piles) - 1
    max_number = 0 
    
    for i in range(len(piles) // 3):
        max_number += sorted_piles[end_idx - (i*2) - 1]
    return max_number
  
  
  
  # https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
