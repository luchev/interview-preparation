#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <set>
#include <vector>
using namespace std;

/**
 * Complexity (n = number of queries)
 * Time complexity: O(n * log(n))
 * Space complexity: O(n)
 */
int main() {
    int queries;
    cin >> queries;
    set<int> heap;
    for (int i = 0; i < queries; i++) {
        int operation;
        cin >> operation;
        if (operation == 1) {
            int add;
            cin >> add;
            heap.insert(add);
        } else if (operation == 2) {
            int remove;
            cin >> remove;
            auto pos = heap.find(remove);
            heap.erase(pos);
        } else if (operation == 3) {
            cout << *heap.begin() << "\n";
        }
    }
    return 0;
}
