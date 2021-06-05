# Complexity (n = number of candidates)
# Time complexity: O(n * log(n))
# Space complexity: O(n)

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        candidates = reversed(sorted(zip(efficiency, speed)))
        result = 0
        speed_sum = 0
        speed_heap = []
        for eff, spd in candidates:
            if len(speed_heap) > k - 1:
                speed_sum -= heapq.heappop(speed_heap)
            heapq.heappush(speed_heap, spd)
            
            speed_sum += spd
            result = max(result, speed_sum * eff)
        
        return result % (10 ** 9 + 7)