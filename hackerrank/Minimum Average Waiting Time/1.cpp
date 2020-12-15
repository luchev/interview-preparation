#include <bits/stdc++.h>
using namespace std;

/**
 * Complexity (n = customers)
 * Time complexity: O(n * log(n))
 * Space complexity: O(n)
 */
struct Order {
    int64_t startTime;
    int64_t waitTime;
    bool operator<(const Order& rhs) const {
        return waitTime > rhs.waitTime;
    }
};

struct Customer {
    int64_t startTime;
    int64_t waitTime;
    bool operator<(const Customer& rhs) const {
        return startTime > rhs.startTime;
    }
};

int64_t minimumAverage(vector<vector<int>> customers) {
    if (customers.empty()) {
        return 0;
    }

    priority_queue<Customer> customersHeap;
    for (auto i : customers) {
        customersHeap.push({i[0], i[1]});
    }

    priority_queue<Order> ordersHeap;
    int64_t totalTime = 0;
    int64_t currentTime = -1;

    while (!ordersHeap.empty() || !customersHeap.empty()) {
        if (ordersHeap.empty()) {
            ordersHeap.push({customersHeap.top().startTime, customersHeap.top().waitTime});
            currentTime = ordersHeap.top().startTime;
            customersHeap.pop();
        } else {
            // cout << (customersHeap.top().startTime) << " " << currentTime << "\n";
            while (!customersHeap.empty() && customersHeap.top().startTime <= currentTime) {
                // cout << "Add " << customersHeap.top().startTime << "\n";
                ordersHeap.push({customersHeap.top().startTime, customersHeap.top().waitTime});
                customersHeap.pop();
            }

            currentTime += ordersHeap.top().waitTime;
            totalTime += currentTime - ordersHeap.top().startTime;
            // cout << ordersHeap.top().startTime << " " << currentTime << " " << totalTime << "\n";
            ordersHeap.pop();

            while (!customersHeap.empty() && customersHeap.top().startTime <= currentTime) {
                // cout << "Add " << customersHeap.top().startTime << "\n";
                ordersHeap.push({customersHeap.top().startTime, customersHeap.top().waitTime});
                customersHeap.pop();
            }
        }
    }

    return totalTime / customers.size();
}

int main() {
    ofstream fout(getenv("OUTPUT_PATH"));
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    vector<vector<int>> customers(n);
    for (int customers_row_itr = 0; customers_row_itr < n; customers_row_itr++) {
        customers[customers_row_itr].resize(2);
        for (int customers_column_itr = 0; customers_column_itr < 2; customers_column_itr++) {
            cin >> customers[customers_row_itr][customers_column_itr];
        }
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }
    int64_t result = minimumAverage(customers);
    fout << result << "\n";
    fout.close();
    return 0;
}
