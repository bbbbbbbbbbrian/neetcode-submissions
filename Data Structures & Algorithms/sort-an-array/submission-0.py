class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(lst1: List[int], lst2: Listp[int]) -> List[int]:
            retlist = []

            while len(lst1) != 0 or len(lst2) != 0:
                if len(lst1) == 0:
                    while len(lst2) != 0:
                        retlist.append(lst2.pop(0))
                if len(lst2) == 0:
                    while len(lst1) != 0:
                        retlist.append(lst1.pop(0))
                if len(lst1) != 0 and len(lst2) != 0:
                    if lst1[0] > lst2[0]:
                        retlist.append(lst2.pop(0))
                if len(lst1) != 0 and len(lst2) != 0:
                    if lst1[0] <= lst2[0]:
                        retlist.append(lst1.pop(0))

            return retlist

        if len(nums) <= 1:
            return nums
        
        left = self.sortArray(nums[0:len(nums)//2])
        right = self.sortArray(nums[len(nums)//2: len(nums)])

        return merge(left,right)