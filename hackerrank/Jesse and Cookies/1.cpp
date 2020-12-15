#include <bits/stdc++.h>
using namespace std;

/**
 * Complexity (n = cookies)
 * Time complexity: O(n * log(n))
 * Space complexity: O(n)
 */
struct minInt {
    int data;
    bool operator<(const minInt &rhs) const {
        return data > rhs.data;
    }
};
int cookies(int k, vector<int> A) {
    priority_queue<minInt> heap;
    for (auto number : A) {
        heap.push({number});
    }

    int turns = 0;
    while (heap.size() > 1 && heap.top().data < k) {
        int a = heap.top().data;
        heap.pop();
        int b = heap.top().data;
        heap.pop();
        heap.push({a + b * 2});
        turns++;
    }

    if (heap.top().data >= k) {
        return turns;
    } else {
        return -1;
    }
}

vector<string> split_string(string);

int main() {
    ofstream fout(getenv("OUTPUT_PATH"));
    string nk_temp;
    getline(cin, nk_temp);
    vector<string> nk = split_string(nk_temp);
    int n = stoi(nk[0]);
    int k = stoi(nk[1]);
    string A_temp_temp;
    getline(cin, A_temp_temp);
    vector<string> A_temp = split_string(A_temp_temp);
    vector<int> A(n);
    for (int A_itr = 0; A_itr < n; A_itr++) {
        int A_item = stoi(A_temp[A_itr]);
        A[A_itr] = A_item;
    }
    int result = cookies(k, A);
    fout << result << "\n";
    fout.close();
    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [](const char &x, const char &y) {
        return x == y and x == ' ';
    });
    input_string.erase(new_end, input_string.end());
    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }
    vector<string> splits;
    char delimiter = ' ';
    size_t i = 0;
    size_t pos = input_string.find(delimiter);
    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));
        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }
    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));
    return splits;
}
