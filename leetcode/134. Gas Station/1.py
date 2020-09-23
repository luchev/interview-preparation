# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        fuel = 0
        starting_station = 0
        difference = 0
        for current_station in range(len(gas)):
            fuel += gas[current_station]
            fuel -= cost[current_station]
            difference += gas[current_station] - cost[current_station]
            if fuel < 0:
                fuel = 0
                starting_station = current_station + 1

        if difference < 0:
            return -1
        return starting_station
