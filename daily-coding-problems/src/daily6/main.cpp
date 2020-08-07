#include "linked_list.hpp"
#include <iostream>

using namespace std;

int main() {
    XORLL ll;
    ll.add(0);
    ll.add(1);
    ll.add(2);
    ll.add(3);
    if (ll.get(0) == 0 && ll.get(1) == 1 && ll.get(2) == 2 &&
    ll.get(3) == 3 && ll.get(4) == -1) {
        cout << "Success!\n";
    } else {
        cout << "Fail!\n";
    }
}