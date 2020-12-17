/**
 * Complexity (n = number of vertices, k = number of edges)
 * Time complexity: O(n + k)
 * Space complexity: O(n)
 */

#include <bits/stdc++.h>
using namespace std;

class Solution {
   public:
    vector<int> colors;
    vector<int> visited;
    bool isBipartite(vector<vector<int>>& graph) {
        colors = vector<int>(graph.size(), 0);
        visited = vector<int>(graph.size(), 0);

        for (auto i = 0; i < graph.size(); i++) {
            if (dfs(i, graph) == false) {
                return false;
            }
        }

        for (auto x : colors) {
            cout << x << ' ';
        }

        return true;
    }

    bool dfs(int current, vector<vector<int>>& edge_list) {
        if (visited[current]) {
            return true;
        }
        visited[current] = true;

        if (colors[current] == 0) {
            colors[current] = 1;
            for (auto neigh : edge_list[current]) {
                colors[neigh] = -colors[current];
                if (!dfs(neigh, edge_list)) {
                    return false;
                }
            }
        } else {
            int color = colors[current];
            for (auto neigh : edge_list[current]) {
                if (colors[neigh] != 0 && colors[neigh] == color) {
                    return false;
                }
                colors[neigh] = -color;
                if (!dfs(neigh, edge_list)) {
                    return false;
                }
            }
        }
        return true;
    }
};
