class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        visiting = set()
        visited = set()
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, parent):
            if node in visiting:
                return False
            
            if node in visited:
                return True
            
            visiting.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            return True
        
        if not dfs(0, -1):
            return False
        
        print(len(visited))

        return True if len(visited) == n else False
        