class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)
        
        visiting = set()
        visited = set()
        res = []

        def dfs(node):
            if node in visiting:
                return False
            
            if node in visited:
                return True
            
            visiting.add(node)

            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            res.append(node)
            return True

        for node in range(numCourses):
            if not dfs(node):
                return []
        
        return res