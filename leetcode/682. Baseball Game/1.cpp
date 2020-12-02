/**
 * Complexity (n = input array size)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */

#include <vector>
#include <string>
using namespace std;
class Solution {
   public:
    int calPoints(vector<string>& ops) {
        vector<int> stak;
        for (auto op : ops) {
            if (op == "+") {
                stak.push_back(stak[stak.size() - 1] + stak[stak.size() - 2]);
            } else if (op == "D") {
                stak.push_back(2 * stak[stak.size() - 1]);
            } else if (op == "C") {
                stak.pop_back();
            } else {
                stak.push_back(stoi(op));
            }
        }

        int sum = 0;
        for (auto x : stak) {
            sum += x;
        }
        return sum;
    }
};
