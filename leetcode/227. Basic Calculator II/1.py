# Complexity (n = tokens in the list (numbers or ops))
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List
import re

class Solution:
    def calculate(self, s: str) -> int:
        tokens = [x.strip() for x in re.split('(\+|/|\-|\*)', s)]

        ops = []
        nums = []

        for token in tokens:
            try:
                nums.append(int(token))
                if ops and ops[-1] == '-':  # don't use subtraction
                    nums[-1] *= -1
                    ops[-1] = '+'
                if ops and ops[-1] in ['*', '/']:  # greedy evaluation when we can
                    nums.append(evalSimple(ops.pop(), nums))
            except:
                while ops and token in ['-', '+'] and ops[-1] in ['*', '/']:
                    nums.append(evalSimple(ops.pop(), nums))
                ops.append(token)

        while ops:
            nums.append(evalSimple(ops.pop(), nums))

        return nums[-1]


def evalSimple(operation, nums):
    a = nums.pop()
    b = nums.pop()
    if operation == '+':
        return b + a
    elif operation == '*':
        return b * a
    elif operation == '/':
        if b < 0:  # handle the division with negative numbers because of rounding
            return -(-b // a)
        else:
            return b // a
    else:
        return 0
