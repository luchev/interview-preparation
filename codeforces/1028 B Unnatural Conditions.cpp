#include <iostream>

int main() {
    int n;
    int m;
    std::cin >> n >> m;

    for (int i = 0; i < 300; i++) {
        std::cout << '4';
    }

    std::cout << std::endl;

    for (int i = 0; i < 299; i++) {
        std::cout << '5';
    }
    std::cout << '6';
}
