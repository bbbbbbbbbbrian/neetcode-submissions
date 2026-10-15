class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in range(len(strs)):
            temp = "".join(sorted(strs[i]))
            if temp not in dict:
                dict[temp] = [strs[i]]
            else:
                dict[temp].append(strs[i])
        
        final = []
        for i in dict:
            final.append(dict[i])

        return final