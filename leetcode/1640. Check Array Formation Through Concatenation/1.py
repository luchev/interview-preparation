# Complexity (n = items in the array)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        i = 0
        pieces_map = { piece[0]: piece for piece in pieces }
        while i < len(arr):
            if arr[i] not in pieces_map:
                return False
            
            current_piece = pieces_map[arr[i]]
            for x in current_piece:
                if arr[i] != x:
                    return False
                i += 1
        return True
