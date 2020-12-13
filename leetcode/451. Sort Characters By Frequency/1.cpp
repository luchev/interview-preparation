/**
 * Complexity (n = lenght of input string)
 * Time complexity: O(n)
 * Space complexity: O(1) because the alphabet is limited to ascii
 */

#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> counter;
        for (auto x : s) {
            counter[x] += 1;
        }
        
        sort(s.begin(), s.end(), [&counter](auto lhs, auto rhs){
            return counter[lhs] > counter[rhs]
                ||(counter[lhs] == counter[rhs] && lhs > rhs);
        });
        
        return s;
    }
};
