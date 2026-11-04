class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        ptr1 = 0
        ptr2 = len(heights) - 1
        while ptr1 < ptr2:
            smaller = min(heights[ptr1], heights[ptr2])
            volume = (ptr2 - ptr1) * smaller
            if max < volume:
                max = volume
            if smaller == heights[ptr1]:
                ptr1 += 1
            else:
                ptr2 -= 1
        return max
