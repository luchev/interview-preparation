# Complexity (n = number of rooms, k = number of keys)
# Time complexity: O(n + k)
# Space complexity: O(n + k)

from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_rooms = [False] * len(rooms)
        
        keys = [0]
        while len(keys):
            current_key = keys.pop()
            if visited_rooms[current_key]:
                continue
            visited_rooms[current_key] = True
            for key in rooms[current_key]:
                keys.append(key)
        
        return all(visited_rooms)
