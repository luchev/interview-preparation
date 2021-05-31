# Complexity (n = number of items in the list)
# Time complexity: O(n * log(n) + m * log(n))
# Space complexity: O(1)

from typing import List
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        left = 0
        for i in range(1, len(searchWord)+1):
            prefix = searchWord[:i]
            left = bisect.bisect_left(products, prefix, 0)
            result.append([])
            for k in range(left, min(left + 3, len(products))):
                if len(products[k]) < len(prefix) or prefix != products[k][:len(prefix)]:
                    break
                result[-1].append(products[k])
        return result
