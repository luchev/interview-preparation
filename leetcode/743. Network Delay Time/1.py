# Complexity(n = number of nodes, v = number of edges = | times |)
# Time complexity: O(v * log n)
# Space complexity: O(v * log n)

from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times, N, K):
        elapsed_time = [0] + [float("inf")] * N
        graph = defaultdict(list)
        heap = [(0, K)]
        for u, v, w in times:
            graph[u].append((v, w))
        while heap:
            time, node = heapq.heappop(heap)
            if time < elapsed_time[node]:
                elapsed_time[node] = time
                for v, w in graph[node]:
                    heapq.heappush(heap, (time + w, v))
        mx = max(elapsed_time)
        return mx if mx < float("inf") else -1
