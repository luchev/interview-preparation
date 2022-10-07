# Complexity (n = input number)
# Time complexity: O(log(n))
# Space complexity: O(log(n))

class Solution:
    def isHappy(self, n: int) -> bool:
        previous = set()
        while n != 1:
            n = sum([int(x) ** 2 for x in str(n)])
            if n in previous:
                break
            previous.add(n)
            
        return n == 1
