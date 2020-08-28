# Complexity (n = length of numbers list)
# Time complexity: O(n^2)
# Space complexity: O(n) this excludes the space for the output array
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = set()
        
        numbers = {}
        for num in nums:
            if num in numbers:
                numbers[num] += 1
            else:
                numbers[num] = 1
        
        if 0 in numbers and numbers[0] >= 3:
            solutions.add((0,0,0))
        
        for keyA, valA in numbers.items():
            for keyB, valB in numbers.items():
                if keyA == keyB and valA < 2:
                    continue
                compliment = 0 - (keyA + keyB)
                if compliment != keyA and compliment != keyB and compliment in numbers:
                    tripplet = [keyA, keyB, compliment]
                    tripplet.sort()
                    tripplet = tuple(tripplet)
                    solutions.add(tripplet)
            
                            
        return solutions
