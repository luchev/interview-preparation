# Complexity (n = length of array, g = #gets, s = #sets)
# Time complexity: O(n + g + s)
# Space complexity: O(n + s)

import bisect

class SnapshotArray:

    def __init__(self, length: int):
        self.cur_snap = 0
        self.arr = [ [[0, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        if self.arr[index][-1][0] == self.cur_snap:
            self.arr[index][-1][1] = val
        else:
            self.arr[index].append([self.cur_snap, val])

    def snap(self) -> int:
        self.cur_snap += 1
        return self.cur_snap - 1

    def get(self, index: int, snap_id: int) -> int:
        maybe = bisect.bisect(self.arr[index], snap_id, key=lambda x: x[0])
        return self.arr[index][maybe - 1][1]

