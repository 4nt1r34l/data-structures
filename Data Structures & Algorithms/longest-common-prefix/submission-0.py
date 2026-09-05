class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        small, large = strs[0], strs[-1]
        res = ""
        for i in range(len(small)):
            if small[i] != large[i]:
                return res
            res+=small[i]
        return res