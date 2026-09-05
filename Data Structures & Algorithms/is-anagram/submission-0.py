class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = Counter(s)

        for char in t:
            if char not in freq:
                return False
            
            freq[char] -= 1
            if freq[char] == 0:
                del freq[char]
        
        return True