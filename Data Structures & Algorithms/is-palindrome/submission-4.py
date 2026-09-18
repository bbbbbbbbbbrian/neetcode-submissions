class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        st = s.lower()
        while i < j:
            while i < len(st) and not st[i].isalnum(): 
                i += 1
            while j > 0 and not st[j].isalnum(): 
                j -= 1
            if i < len(st) and j > 0 and st[i] != st[j]:
                return False
            i+=1
            j-=1
        return True
