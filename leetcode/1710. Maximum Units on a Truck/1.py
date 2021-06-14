# Complexity (n = length of boxTypes)
# Time complexity: O(n * log(n))
# Space complexity: O(n)

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        result = 0
        for count, value in boxTypes:
            take = min(count, truckSize)
            result += take * value
            truckSize -= take
        return result