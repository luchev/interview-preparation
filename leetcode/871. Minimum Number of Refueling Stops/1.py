# Complexity (n = number of stations)
# Time complexity: O(n * log(n))
# Space complexity: O(n)

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = []
        stations = [(0, 0)] + stations + [(target, 0)]
        result = 0
        fuel = startFuel
        for i in range(1, len(stations)):
            fuel -= stations[i][0] - stations[i - 1][0]
            while len(heap) > 0 and fuel < 0:
                fuel += -heapq.heappop(heap)
                result += 1
            if fuel < 0:
                return -1
            heappush(heap, -stations[i][1])
        return result