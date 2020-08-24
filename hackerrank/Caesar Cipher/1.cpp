#include <bits/stdc++.h>
using namespace std;

bool isLowerCase(char c) {
    return 'a' <= c && c <= 'z';
}

bool isUpperCase(char c) {
    return 'A' <= c && c <= 'Z';
}

/**
 * Complexity (n = array length)
 * Time complexity: O(n)
 * Space complexity: O(1)
 */
string caesarCipher(string s, int k) {
    for (char& c : s) {
        if (isUpperCase(c)) {
            c = ((c - 'A') + k) % ('Z' - 'A' + 1) + 'A';
        } else if (isLowerCase(c)) {
            c = ((c - 'a') + k) % ('z' - 'a' + 1) + 'a';
        }
    }
    return s;
}

int main() {
    ofstream fout(getenv("OUTPUT_PATH"));
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    string s;
    getline(cin, s);
    int k;
    cin >> k;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    string result = caesarCipher(s, k);
    fout << result << "\n";
    fout.close();
    return 0;
}
