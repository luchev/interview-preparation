# Complexity (n = length of all words in A, k = length of all words in B)
# Time complexity: O(n + k)
# Space complexity: O(ALPHABET_SIZE)

from typing import List
from collections import Counter

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        bCounts = defaultdict(int)
        for word in B:
            for char, count in Counter(word).items():
                bCounts[char] = max(bCounts[char], count)
        
        universals = []
        for word in A:
            aCounts = Counter(word)
            bChecked = 0
            isUniversal = True
            for char, count in aCounts.items():
                if char in bCounts:
                    bChecked += 1
                    if aCounts[char] < bCounts[char]:
                        isUniversal = False
                        break
                    
            if isUniversal and bChecked == len(bCounts):
                universals.append(word)
        return universals
