class Solution:
    def reverseString(self, s: List[str]) -> None:
        idx1 = 0
        idx2 = len(s) - 1
        while(idx1 < idx2):
            s[idx1], s[idx2] = s[idx2], s[idx1]
            idx1 += 1
            idx2 -= 1
            
        