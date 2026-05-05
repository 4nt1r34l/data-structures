from heapq import heappop, heappush
from collections import defaultdict, deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, dst, cost in times:
            graph[src].append((dst, cost)) # [(destination, cost)]
        
        minHeap = [(0, k)] # [(cost, node)]
        shortest = {}
        while minHeap:
            cost, node = heappop(minHeap)

            if node in shortest:
                continue
            
            shortest[node] = cost

            for dst, c in graph[node]:
                if dst not in shortest:
                    heappush(minHeap, (c+cost, dst))
        
        return max(shortest.values()) if len(shortest) == n else -1
