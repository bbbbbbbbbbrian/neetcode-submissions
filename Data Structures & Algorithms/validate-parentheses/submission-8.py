class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        lst = []
        brackets = {'(':')','{':'}','[':']'}
        for i in s:
            if i in brackets:
                lst.append(i)
            elif len(lst) == 0:
                return False
            else:
                value = lst.pop()
                if(i != brackets[value]):
                    return False
        if len(lst) != 0:
            return False
        return True

        