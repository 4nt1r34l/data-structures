from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visit = set()
        count = 0

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(graph, node, visit):
            if node in visit:
                return False
            
            visit.add(node)

            for nei in graph[node]:
                dfs(graph, nei, visit)
            
            return True
        
        for i in range(n):
            if dfs(graph, i, visit):
                count+=1
        
        return count
