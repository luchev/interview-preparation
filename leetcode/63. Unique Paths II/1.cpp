#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int rows = obstacleGrid.size();
        if (rows == 0) {
            return 0;
        }
        int cols = obstacleGrid[0].size();
        
        vector<vector<long long>> dp;
        
        for (auto &row : obstacleGrid) {
            vector<long long> current_row;
            for (auto &x : row) {
                current_row.push_back(x * -1);
            }
            dp.push_back(current_row);
        }
        
        if (dp[0][0] == -1) {
            return 0;
        }
        
        for (int col = cols - 1; col >= 0; col--) {
            if (dp[rows -1][col] == -1) {
                break;
            }
            dp[rows -1][col] = 1;
        }
        
        for (int row = rows - 1; row >= 0; row--) {
            if (dp[row][cols - 1] == -1) {
                break;
            }
            dp[row][cols - 1] = 1;
        }
        
        for (int row = rows - 2; row >= 0; row--) {
            for (int col = cols - 2; col >= 0; col--) {
                if (dp[row][col] == -1) {
                    continue;
                }
                
                if (dp[row + 1][col] != -1) {
                    dp[row][col] += dp[row + 1][col];
                }
                
                if (dp[row][col + 1] != -1) {
                    dp[row][col] += dp[row][col + 1];
                }
                
            }
        }
        
        return dp[0][0];
    }
};
