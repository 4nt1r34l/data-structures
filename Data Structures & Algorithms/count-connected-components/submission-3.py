class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        graph = defaultdict(list)
        c = 0

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, visit):
            if node in visit:
                return False
            
            visit.add(node)

            for nei in graph[node]:
                if nei not in visit:
                    dfs(nei, visit)
            
            return True
        
        for i in range(n):
            if i not in visit:
                dfs(i, visit)
                c+=1
        
        return c


            
