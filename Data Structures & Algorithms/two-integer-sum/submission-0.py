class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        numbers[nums[0]] = 0
        for i in range(1, len(nums)):
            need = target - nums[i]
            if need in numbers:
                return [min(numbers[need],i),max(numbers[need],i)]
            if nums[i] not in numbers:
                numbers[nums[i]] = i


            

