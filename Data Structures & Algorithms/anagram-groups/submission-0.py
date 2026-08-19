class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)

        for i in range(len(strs)):
            word = "".join(sorted(strs[i]))
            freq[word].append(strs[i])
        
        return list(freq.values())