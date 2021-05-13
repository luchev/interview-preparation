# Complexity (n = number of boxes, m = number of warehouses)
# Time complexity: O(n * log(n) + m)
# Space complexity: O(m)

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        mins = [warehouse[0]]
        for x in warehouse[1:]:
            mins.append(min(x, mins[-1]))
        
        boxes.sort()
        result = 0
        for box in boxes:
            if len(mins) == 0:
                break
            
            while len(mins) > 0 and mins[-1] < box:
                mins.pop()
                
            if len(mins) > 0 and box <= mins[-1]:
                result += 1
                mins.pop()
            
        return result