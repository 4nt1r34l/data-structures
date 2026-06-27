class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = Counter(t)

        for c in s:
            if c in count:
                count[c]-=1
                if count[c] == 0:
                    del count[c]
        
        return "".join(list(count.keys()))