class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        for i in nums:
            if i not in numbers:
                numbers[i] = 1
            else:
                numbers[i] += 1

        return sorted(numbers, key=numbers.get, reverse=True)[:k]
