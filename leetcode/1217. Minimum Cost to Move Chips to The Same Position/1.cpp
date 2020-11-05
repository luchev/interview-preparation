/**
 * Complexity (n = input array size)
 * Time complexity: O(n)
 * Space complexity: O(1)
 */
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
   public:
    int minCostToMoveChips(vector<int>& position) {
        int odds = 0;
        int evens = 0;
        for (auto x : position) {
            if (x >> 1 << 1 == x) {
                evens++;
            } else {
                odds++;
            }
        }
        return min(odds, evens);
    }
};
