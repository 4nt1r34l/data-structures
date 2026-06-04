class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,dist in times:
            graph[u].append((v,dist)) # [(v,dist)]
        
        min_times = {}
        min_heap = [(0, k)]

        while min_heap:
            distance, source = heapq.heappop(min_heap)

            if source in min_times:
                continue
            
            min_times[source] = distance

            for node, dist in graph[source]:
                if node not in min_times:
                    heapq.heappush(min_heap, (distance+dist, node))
        
        return max(min_times.values()) if len(min_times) == n else -1
            


