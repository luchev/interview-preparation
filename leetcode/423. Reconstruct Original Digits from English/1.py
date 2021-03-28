# Complexity (n = length of input string)
# Time complexity: O(n)
# Space complexity: O(1)

import collections

class Solution:
    def originalDigits(self, s: str) -> str:
        # Need to greedily take numbers in this order
        # six seven five four two zero one nine eight three
        nums = [
            (6,'six','x'),
            (7,'seven','s'),
            (5,'five', 'v'),
            (4,'four','f'),
            (2,'two','w'),
            (0,'zero','z'),
            (1,'one','o'),
            (3,'three','r'),
            (8,'eight','h'),
            (9,'nine','i')
        ]
        
        letters = collections.Counter(s)
        counts = [0] * 10
        for n, word, pull in nums: # pull is the unique letter for this number
            npull = letters[pull]
            counts[n] = npull
            for char in word:
                letters[char] -= npull
        
        return ''.join(str(i) * count for i, count in enumerate(counts))
