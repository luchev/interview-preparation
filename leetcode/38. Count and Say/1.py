# Complexity (n = times to repeat the counting)
# Time complexity: O(2^n)
# Space complexity: O(2^n)

from typing import List

class Solution:
    def countAndSay(self, n: int) -> str:
        return ''.join(say(['1'], n))

def say(num: List[str], n: int) -> str:
    if n == 1:
        return num
    counted = []
    current = num[0]
    current_count = 1
    for i in range(1, len(num)):
        if num[i] != current:
            counted.append(str(current_count))
            counted.append(current)
            current = num[i]
            current_count = 1
        else:
            current_count += 1

    counted.append(str(current_count))
    counted.append(current)
    return say(counted, n - 1)
