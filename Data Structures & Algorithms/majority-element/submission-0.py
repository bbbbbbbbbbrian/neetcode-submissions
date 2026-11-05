class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sorted = nums.sort()
        return(nums[len(nums)//2])