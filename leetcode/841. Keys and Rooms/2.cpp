/**
 * Complexity (n = number of rooms, k = number of keys)
 * Time complexity: O(n + k)
 * Space complexity: O(n + k)
 */

#include <bits/stdc++.h>
using namespace std;

class Solution {
   public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        vector<bool> unlocked(rooms.size(), false);
        unlocked[0] = true;

        vector<bool> visited(rooms.size(), false);

        stack<int> frontier;
        frontier.push(0);
        while (frontier.size() != 0) {
            int current_room = frontier.top();
            frontier.pop();
            if (visited[current_room]) {
                continue;
            }
            cout << current_room << '\n';
            visited[current_room] = true;

            for (auto key : rooms[current_room]) {
                unlocked[key] = true;
                frontier.push(key);
            }
        }

        for (auto room : visited) {
            if (room == false) {
                return false;
            }
        }
        return true;
    }
};
