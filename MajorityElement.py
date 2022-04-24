

def majority(nums):
  return sorted(nums)[len(nums) // 2]



# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# or 

def majorityElement(self, nums: List[int]) -> int:
        for i in set(nums):
            if nums.count(i) > (len(nums) / 2):
                return i
