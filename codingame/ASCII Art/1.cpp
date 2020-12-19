#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int L;
    cin >> L; cin.ignore();
    int H;
    cin >> H; cin.ignore();
    string target;
    getline(cin, target);
    for_each(target.begin(), target.end(), [](char & c) { c= toupper(c); } );
    vector<string> rows;
    for (int i = 0; i < H; i++) {
        string ROW;
        getline(cin, ROW);
        rows.push_back(ROW);
    }

    for (int row = 0; row < H; row++) {
        for (int letter = 0; letter < target.size(); letter++) {
            int startPosition = (target[letter] - 'A') * L;
            if (target[letter] < 'A' || target[letter] > 'Z') {
                startPosition = ('Z' - 'A' + 1) * L;
            }
            for (int position = startPosition; position < startPosition + L; position++) {
                cout << rows[row][position];
            }
        }
        cout << endl;
    }
}
