#include <bits/stdc++.h>
using namespace std;

/**
 * Complexity (n = count of numbers)
 * Time complexity: O(n * log(n))
 * Space complexity: O(n)
 */
struct minInt {
    int data;
    bool operator<(const minInt& rhs) const {
        return data > rhs.data;
    }
};

struct maxInt {
    int data;
    bool operator<(const maxInt& rhs) const {
        return data < rhs.data;
    }
};

vector<double> runningMedian(vector<int> a) {
    vector<double> medians;
    priority_queue<minInt> minHeap;
    priority_queue<maxInt> maxHeap;
    for (auto number : a) {
        if (minHeap.size() == maxHeap.size()) {
            if (maxHeap.size() > 0 && maxHeap.top().data > number) {
                int tempExtracted = maxHeap.top().data;
                maxHeap.pop();
                maxHeap.push({number});
                number = tempExtracted;
            }
            minHeap.push({number});
            medians.push_back(minHeap.top().data);
        } else {
            int tempExtracted = minHeap.top().data;
            minHeap.pop();
            minHeap.push({max(tempExtracted, number)});
            maxHeap.push({min(tempExtracted, number)});
            medians.push_back((minHeap.top().data + maxHeap.top().data) / 2.0);
        }
    }
    return medians;
}

int main() {
    int a_count;
    cin >> a_count;
    vector<int> a;
    for (int i = 0; i < a_count; i++) {
        int input;
        cin >> input;
        a.push_back(input);
    }
    vector<double> result = runningMedian(a);
    for (unsigned i = 0; i < result.size(); i++) {
        cout << std::fixed;
        cout << std::setprecision(1);
        cout << result[i] << "\n";
    }
    return 0;
}
