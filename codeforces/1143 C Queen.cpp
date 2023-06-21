#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

struct Node {
public:
    int index;
    bool respects;

    Node(int index, bool respects) {
        this->index = index;
        this->respects = respects;
    }
};

int main() {
    int rows = 0;
    std::cin >> rows;

    std::vector<int> parents;
    std::vector<std::vector<Node> > tree;
    std::vector<bool> respects;

    int root = -1;
    for (int i = -1; i < rows; i++) {
        tree.push_back(std::vector<Node>());
        respects.push_back(true);
        parents.push_back(-1);
    }

    for (int row = 0; row < rows; row++) {
        int parent;
        int respect;

        std::cin >> parent >> respect;
        if (respect == 1) {
            respects[row + 1] = false;
        }
        if (parent == -1) {
            root = row;
            continue;
        }
        parents[row + 1] = parent;
        tree[parent].push_back(Node(row + 1, respect == 0));
    }

    bool atLeastOncePrinted = false;
    for (int i = 1; i < tree.size(); i++) {
        bool print = true;
        if (respects[i]) {
            print = false;
        }
        for (auto x : tree[i]) {
            if (x.respects) {
                print = false;
            }
        }

        if (print) {
            atLeastOncePrinted = true;
            std::cout << i << " ";
        }
    }

    if (!atLeastOncePrinted) {
        std::cout << -1;
    }

}

