/**
 * Complexity (n = vector size)
 * Time complexity: O(log(n))
 * Space complexity: O(1)
 */

#include <vector>
using namespace std;
class Solution {
   public:
    int search(const vector<int>& haystack, int needle) {
        int left = 0;
        int right = haystack.size() - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (haystack[mid] == needle) {
                return mid;
            } else if (haystack[mid] < needle) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }
};
