
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u,v in prerequisites:
            graph[u].append(v)

        
        visiting = set()
        visited = set()

        for i in range(numCourses):

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
                return True
            
            if not dfs(i):
                return False
        
        return True




