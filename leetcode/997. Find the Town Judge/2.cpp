/**
 * Complexity (n = number of people, k = number of edges)
 * Time complexity: O(n + k)
 * Space complexity: O(n + k)
 */

#include <bits/stdc++.h>
using namespace std;

class Solution {
   public:
    int findJudge(int N, vector<vector<int>>& trust) {
        unordered_map<int, unordered_set<int>> trust_map;
        unordered_set<int> potential_judges;
        for (int i = 1; i <= N; i++) {
            potential_judges.insert(i);
        }

        for (auto trust_pair : trust) {
            trust_map[trust_pair[0]].insert(trust_pair[1]);
            potential_judges.erase(trust_pair[0]);
        }

        if (potential_judges.size() != 1) {
            return -1;
        }

        int potential_judge = *potential_judges.begin();

        for (auto x : trust_map) {
            if (x.second.count(potential_judge) == 0) {
                return -1;
            }
        }

        return potential_judge;
    }
};
