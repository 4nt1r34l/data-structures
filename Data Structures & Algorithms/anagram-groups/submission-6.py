class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for char in strs:
            word = "".join(sorted(char))
            anagram[word].append(char)
        
        return list(anagram.values())