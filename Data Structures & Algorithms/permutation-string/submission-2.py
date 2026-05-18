from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False
        
        if s1 == "":
            return True

        freq = Counter(s1)
        count = {}
        left = 0

        for right in range(len(s2)):
            count[s2[right]] = 1 + count.get(s2[right], 0)

            while right-left+1 > len(s1):
                count[s2[left]]-=1
                if count[s2[left]] == 0:
                    del count[s2[left]]
                left+=1
            
            if count == freq:
                return True
        
        return False