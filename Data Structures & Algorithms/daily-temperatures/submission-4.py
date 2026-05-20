class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # (node, i)

        for index, val in enumerate(temperatures):
            while stack and stack[-1][0] < val:
                _, pop_index = stack.pop()
                res[pop_index] = index - pop_index
            stack.append((val, index))
        return res