/**
 * Complexity (x, y)
 * Time complexity: O(x * y)
 * Space complexity: O(x * y)
 */

#include <bits/stdc++.h>
using namespace std;

class Solution {
   public:
    int minKnightMoves(int x, int y) {
        x = abs(x);
        y = abs(y);
        queue<pair<pair<int, int>, int>> next_moves;
        set<pair<int, int>> visited;

        next_moves.push({{0, 0}, 0});
        vector<pair<int, int>> shifts{{-2, 1}, {-1, 2}, {1, 2}, {2, 1}, {1, -2}, {2, -1}};

        while (true) {
            auto front = next_moves.front();
            next_moves.pop();
            auto coords = front.first;
            auto depth = front.second;

            if (coords.first == x && coords.second == y) {
                return depth;
            }

            if (-1 <= coords.first && coords.first <= x + 2 && -1 <= coords.second && coords.second <= y + 2) {
                if (visited.count(coords) == 1) {
                    continue;
                }
                visited.insert(coords);

                for (auto x : shifts) {
                    next_moves.push({{coords.first + x.first, coords.second + x.second}, depth + 1});
                }
            }
        }
        return -1;
    }
};
