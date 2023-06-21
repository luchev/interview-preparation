#include <iostream>
#include <string>

int main() {
    int size;
    std::cin >> size;
    std::string aabb = "aabb";
    int index = 0;
    for (int i = 0; i < size; i++) {
        std::cout << aabb[index];
        index++;
        if (index == 4) {
            index = 0;
        }
    }
}

/*
 * 1 a
 * 2 ab
 * 3 aab
 * 4 aabb
 * 5 aabba
 * 6 aabbaa
 * 7 aabbaab
 * 8 aabbaabb
 *
 */
