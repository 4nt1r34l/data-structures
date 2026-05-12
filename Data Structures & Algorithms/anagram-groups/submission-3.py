class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}

        for char in strs:
            word = "".join(sorted(char))

            if word in freq:
                freq[word].append(char)
            else:
                freq[word] = [char]
        
        return list(freq.values())