#include <iostream>
#include <vector>
using namespace std;

int main() {
    int a;
    int b;
    int c;
    int d;

    cin >> a >> b >> c >> d;

    cout << "50 50\n";
    vector<string> grid = vector<string>(50, string(50, 'D'));
    for (int i = 0; i < 12; i++) {
        grid[i] = string(50, 'A');
    }

    a -= 1;
    d -= 1;

    int row = 0;
    int col = 0;
    for (; d > 0; d--) {
        grid[row][col] = 'D';
        col += 2;
        if (col >= 50) {
            col = 0;
            row += 2;
        }
    }

    row = 13;
    col = 0;

    for (; a > 0; a--) {
        grid[row][col] = 'A';
        col += 2;
        if (col >= 50) {
            col = 0;
            row += 2;
        }
    }

    for (; b > 0; b--) {
        grid[row][col] = 'B';
        col += 2;
        if (col >= 50) {
            col = 0;
            row += 2;
        }
    }

    for (; c > 0; c--) {
        grid[row][col] = 'C';
        col += 2;
        if (col >= 50) {
            col = 0;
            row += 2;
        }
    }

    for (int i = 0; i < 50; i++) {
        std::cout << grid[i] << "\n";
    }

}

/** 1 1 1 3

  AD-D-DDDDDD
  DDDDDDDDDDD
  AD-D-D-DDDD
  DDDDDDDDDDD
  DDDDDDDDDDD
  DDDDDDDDDDD
  AAAAAAAAAAA
  ADADADADA=A
  AAAAAAAAAAA
  A=A=A_A_AAA
  AAAAAAAAAAA


*/
