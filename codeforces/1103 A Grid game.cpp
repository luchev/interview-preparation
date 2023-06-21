#include <iostream>
#include <string>

int main() {
    char in;
    int verticalCol = 1;
    int verticalRow = 3;
    
    int horizontalCol = 1;
    int horizontalRow = 1;
    while (std::cin >> in) {
        if (in == '0') {
            std::cout << verticalRow << ' ' << verticalCol << '\n';
            verticalCol++;
            if (verticalCol == 5) {
                verticalCol = 1;
            }
        } else if (in == '1') {
            std::cout << horizontalRow << ' ' << horizontalCol << '\n';
            horizontalCol += 2;
            if (horizontalCol == 5) {
                horizontalCol = 1;
            }
        }
    }
}
