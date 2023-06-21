#include <iostream>
#include <vector>

struct Node {
    int sum;
    int value;
    int parent;
    Node(int sum = 0, int value = 0, int parent = 0): sum(sum), value(value), parent(parent) {}
};


std::vector<std::vector<int> > children;
std::vector<Node> nodes;

long long result = 0;
bool exists = true;

void dfs(int current) {
    if (nodes[current].value == -1) {
        if (nodes[current].sum == -1) {
            int childrenMin = 1000000001;
            for (int k : children[current]) {
                if (nodes[k].sum < childrenMin) {
                    childrenMin = nodes[k].sum;
                }
            }
            nodes[current].value = childrenMin - nodes[nodes[current].parent].sum;

            if (children[current].size() == 0) {
                nodes[current].value = 0;
            }

        } else {
            nodes[current].value = nodes[current].sum - nodes[nodes[current].parent].sum;
        }
    }

    nodes[current].sum = nodes[nodes[current].parent].sum + nodes[current].value;

    result += nodes[current].value;

    if (nodes[current].value < 0) {
        exists = false;
    }

    // std::cout << current << " " << nodes[current].sum << " " << nodes[current].value << "\n";

    for (auto child : children[current]) {
        dfs(child);
    }
}

int main() {
    int nodesCount = 0;
    std::cin >> nodesCount;

    children.resize(nodesCount + 1);
    nodes.resize(nodesCount + 1);

    std::vector<int> parents;
    parents.push_back(-1);
    parents.push_back(0);

    for (int i = 0; i < nodesCount - 1; i++) {
        int parent;
        std::cin >> parent;
        parents.push_back(parent);
    }

    for (int i = 1; i < nodesCount + 1; i++) {
        int sum;
        std::cin >> sum;
        nodes[i] = Node(sum, -1, parents[i]);
        children[parents[i]].push_back(i);
    }

    nodes[1].value = nodes[1].sum;
    nodes[0].value = 0;
    nodes[0].sum = 0;

    dfs(1);

    if (exists) {
        std::cout << result;
    } else {
        std::cout << -1;
    }
}
