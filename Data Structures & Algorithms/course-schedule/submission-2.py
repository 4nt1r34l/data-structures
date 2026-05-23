class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        visiting = set()
        visited = set()

        for u,v in prerequisites:
            graph[u].append(v)

        def dfs(node):
            if node in visited:
                return True
            
            if node in visiting:
                return False
            
            visiting.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            
            return True
        
        for node in range(numCourses):
            if not dfs(node):
                return False
        
        return True