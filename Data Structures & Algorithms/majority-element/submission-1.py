class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vals = {}
        for i in range(len(nums)):
            if nums[i] not in vals:
                vals[nums[i]] = 1
            else:
                vals[nums[i]] += 1
        
        for i in vals:
            if vals[i] >= len(nums) // 2:
                return i