class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([beginWord])
        ans = 1
        words = set(wordList)

        if endWord not in words:
            return 0
        
        def is_letter_apart(wordA, wordB):
            diff = 0
            for a, b in zip(wordA, wordB):
                if a!=b:
                    diff+=1
                    if diff > 1:
                        return False
            
            return diff == 1
        
        while queue:
            length = len(queue)
            for _ in range(length):
                word = queue.popleft()

                for char in list(words):
                    if is_letter_apart(word, char):
                        if char == endWord:
                            return ans+1
                        queue.append(char)
                        words.remove(char)
            ans+=1
        
        return 0
            