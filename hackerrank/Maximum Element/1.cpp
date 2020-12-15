#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <set>
#include <stack>
#include <vector>
using namespace std;

/**
 * Complexity (n = number of queries)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
int main() {
    vector<int> stak;
    int queries;
    cin >> queries;
    for (int i = 0; i < queries; i++) {
        int instruction;
        cin >> instruction;
        if (instruction == 1) {
            int number;
            cin >> number;
            stak.push_back(number);
        } else if (instruction == 2) {
            stak.pop_back();
        } else {
            int maxVal = INT_MIN;
            for (auto it = stak.begin(); it < stak.end(); it++) {
                if (*it > maxVal) {
                    maxVal = *it;
                }
            }
            cout << maxVal << "\n";
        }
    }
    return 0;
}
