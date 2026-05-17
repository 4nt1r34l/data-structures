class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = [] # [(temp, index)]
        res = [0]*len(temp)

        for index, val in enumerate(temp):
            while stack and stack[-1][0] < val:
                _, i = stack.pop()
                res[i] = index - i
            stack.append((val, index))
        return res