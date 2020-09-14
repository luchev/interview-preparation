/**
 * Complexity (n = number of points)
 * Time complexity: O(n)
 * Space complexity: O(1)
*/

#include <vector>
using namespace std;
class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        if (coordinates[1][0] == coordinates[0][0]) {
            // Check if the line is vertical
            for (int i = 1; i < coordinates.size() - 1; i++) {
                if (coordinates[i][0] != coordinates[i + 1][0]) {
                    return false;
                }
            }
            return true;
        } else {
            // Generate the line equation for the first 2 points and see if it applies to all other points
            double a = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0]);
            double b = coordinates[0][1] - a * coordinates[0][0];

            for (int i = 2; i < coordinates.size(); i++) {
                if (coordinates[i][1] != a * coordinates[i][0] + b) {
                    return false;
                }
            }
            return true;
        }
    }
};
