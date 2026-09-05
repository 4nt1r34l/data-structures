class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)

        for word in strs:
            char = "".join(sorted(word))
            freq[char].append(word)
        
        return list(freq.values())