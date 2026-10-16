class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            string = string + i + "¥"
        return string
    def decode(self, s: str) -> List[str]:
        lst = []
        back = 0
        for i in range(len(s)):
            if s[i] == '¥':
                lst.append(s[back:i])
                back = i + 1
        return lst
