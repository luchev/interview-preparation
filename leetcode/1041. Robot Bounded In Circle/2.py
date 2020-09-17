# Complexity (n = number of instructions)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # directions: N = 0, E = 1, S = 2, W = 3
        moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        position = [0, 0]
        direction = 0

        for inst in instructions:
            if inst == 'G':
                position[0] += moves[direction][0]
                position[1] += moves[direction][1]
            elif inst == 'L':
                direction = (direction - 1) % 4
            elif inst == 'R':
                direction = (direction + 1) % 4

        # if we haven't moved or we have rotated we will stay in a circle
        return position == [0, 0] or direction != 0
