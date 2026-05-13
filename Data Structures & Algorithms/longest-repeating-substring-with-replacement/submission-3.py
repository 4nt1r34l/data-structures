class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        largest, left, maxf = 0,0,0

        for right in range(len(s)):
            freq[s[right]] = 1 + freq.get(s[right],0)
            maxf = max(maxf, freq[s[right]])

            if (right-left+1) - maxf > k:
                freq[s[left]]-=1
                left+=1
            
            largest = max(largest, right-left+1)
        return largest