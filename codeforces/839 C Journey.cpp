#include <iostream>
#include <vector>
#include <iomanip>

std::vector<std::vector<int> > tree(100001);
double result = 0;

void dfs(int parent, int current, int distance, double prob) {
    if (tree[current].size() <= 1) {
        result += prob * distance;
    }
    
    double childProbability = prob / (tree[current].size() - 1);
    for (auto x : tree[current]) {
        if (x != parent) {
            dfs(current, x, distance + 1, childProbability);
        }
    }
}

int main() {
    int rows = 0;
    std::cin >> rows;

    for (int i = 0; i < rows - 1; i++) {
        int a; 
        int b;

        std::cin >> a >> b;
        tree[a].push_back(b);
        tree[b].push_back(a);
    }

    double childProbability = 1.0 / (tree[1].size());
    for (auto x : tree[1]) {
        dfs(1, x, 1, childProbability);
    }



    std::cout << std::setprecision(9) << result;
}
