# Complexity (n = input n)
# Time complexity: O(2^n)
# Space complexity: O(2^n)

class Solution:
    def grayCode(self, n: int) -> List[int]:
        bitmasks = [1 << i for i in range(0, n)]
        flipBitArr = [0]
        for i in range(1, n):
            flipBitArr = flipBitArr + [i] + flipBitArr
        result = [0]
        for flip in flipBitArr:
            result.append(result[-1] ^ bitmasks[flip])
        return result