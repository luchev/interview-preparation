# Complexity (n = number of items in the list)
# Time complexity on average: O(1)
# Time complexity in the worst case: O(inf)
# Space complexity: O(1)

import random

def rand7():
    return random.randint(1, 7)


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        result = 41
        while result >= 41:
            result = (rand7() - 1) * 7 + rand7()

        return result % 10 + 1
