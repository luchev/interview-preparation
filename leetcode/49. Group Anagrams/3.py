# Complexity (n = number of words, m = average word length)
# Time complexity: O(n * m * ALPHABET_SIZE) ALPHABET_SIZE sorting (if we use counting sort)
# Space complexity: O(n * m)

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            groups[''.join(sorted(word))].append(word)
        return groups.values()
