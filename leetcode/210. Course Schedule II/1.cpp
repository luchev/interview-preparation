/**
 * Complexity (n = courses, k = dependencies)
 * Time complexity: O(n + k)
 * Space complexity: O(n + k)
 */

#include <bits/stdc++.h>
using namespace std;

class Solution {
   public:
    vector<int> courses;
    vector<vector<int>> graph;
    vector<char> visited;

    // o = open vertex
    // c = closed vertex
    // u = unvisited vertex
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        graph.resize(numCourses);
        for (auto dependency : prerequisites) {
            int start = dependency[0];
            int end = dependency[1];
            graph[start].push_back(end);
        }

        visited.resize(numCourses, 'u');
        for (int start = 0; start < numCourses; start++) {
            if (dfs(start) == false) {
                return vector<int>();
            }
        }

        return courses;
    }

    bool dfs(int start) {
        if (visited[start] == 'c') {
            return true;
        } else if (visited[start] == 'o') {
            return false;
        }

        visited[start] = 'o';

        for (auto neigh : graph[start]) {
            if (dfs(neigh) == false) {
                return false;
            }
        }

        courses.push_back(start);
        visited[start] = 'c';
        return true;
    }
};
