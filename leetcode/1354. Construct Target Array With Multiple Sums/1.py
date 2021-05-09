# Complexity (n = number of items in input array, k = max(input))
# Time complexity: O(n*log(n)) for the priority queue
# Space complexity: O(n)

from queue import PriorityQueue

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        que = PriorityQueue()
        for x in target:
            que.put(-x)
        
        current_sum = sum(target)
        while que.queue[0] < -1:
            top = -que.get()
            sum_without_top = current_sum - top
            if sum_without_top == 1:
                return True
            if sum_without_top == 0:
                return False
            
            new_top = top % sum_without_top
            if new_top == 0 or new_top == top:
                return False
            current_sum = sum_without_top + new_top
            que.put(-new_top)
            
        return True
