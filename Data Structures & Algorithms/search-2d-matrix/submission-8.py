class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        for i in range(len(matrix) - 1,0,-1):
            if matrix[i][0] <= target:
                row = i
                break
        start = 0
        mid = 0
        end = len(matrix[row]) - 1
        while start <= end:
            mid = (start + end) // 2 
            if matrix[row][mid] > target:
                end = mid - 1
            elif matrix[row][mid] < target:
                start = mid + 1
            elif matrix[row][mid] == target:
                return True

        return False
                

