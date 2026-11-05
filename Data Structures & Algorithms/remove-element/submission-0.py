class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        length = len(nums)
        while val in nums:
            nums.remove(val)
            count += 1

        return  length - count