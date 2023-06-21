#include <iostream>
#include <cmath>

int main() {
    long long houses;
    long long turns;
    long long distance;

    std::cin >> houses >> turns >> distance;

    if (distance > turns * (houses - 1) || turns > distance) {
        std::cout << "NO";
        return 0;
    }

    std::cout << "YES\n";

    long long current = 1;
    while (turns > 0) {
        long long step = std::min(houses - 1, distance - (turns - 1));

        if (current - step > 0) {
            current -= step;
        } else {
            current += step;
        }
        std::cout << current << ' ';

        distance -= step;
        turns--;
    }
}
