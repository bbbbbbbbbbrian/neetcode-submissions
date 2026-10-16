class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        return "¥".join(strs) + "¥"
        
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        lst = []
        back = 0
        for i in range(len(s)):
            if s[i] == '¥':
                lst.append(s[back:i])
                back = i + 1
        return lst
