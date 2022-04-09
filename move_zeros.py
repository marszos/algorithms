# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zeros = nums.count(0)
        non_zero_index = 0 
        
        for n in range(len(nums)):
            if nums[n] != 0:
                nums[non_zero_index] = nums[n]
                non_zero_index += 1 
        
        for zero in range(1,count_zeros +1):
            nums[-zero] = 0 
        
        
        return nums 
