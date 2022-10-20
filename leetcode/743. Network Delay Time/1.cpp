// Complexity(n = number of nodes, v = number of edges = |times|)
// Time complexity : O(v * log n)
// Space complexity : O(v * log n)

struct Edge {
    int end;
    int weight;
    
	bool operator<(const Edge & rhs) const {
		return weight > rhs.weight;
	}
};

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        unordered_map<int, vector<Edge>> graph;
        for (auto edge : times) {
            int start = edge[0];
            int end = edge[1];
            int weight = edge[2];
            graph[start].push_back({end, weight});
        }
        
        
        unordered_set<int> visited;
        unordered_map<int, int> delay;
        for (int i = 1; i <= n; i++) {
            delay[i] = 1000000;
        }
        priority_queue<Edge> que;
        que.push({k, 0});
        delay[k] = 0;
        
        while (!que.empty()) {
            auto current = que.top();
            que.pop();
            int currentNode = current.end;
            
            if (visited.count(currentNode) > 0) {
                continue;
            }
            visited.insert(currentNode);
            
            for (auto edge : graph[currentNode]) {
                int neighbour = edge.end;
                int weight = edge.weight;
                if (delay[neighbour] > delay[current.end] + weight) {
                    que.push({edge.end, delay[current.end] + weight});
                    delay[neighbour] = delay[current.end] + weight;
                }
            }
        }
        
        if (delay.size() != n) {
            return -1;
        } else {
            int max = 0;
            for (auto x : delay) {
                if (x.second > max) {
                    max = x.second;
                }
            }
            if (max == 1000000) {
                return -1;
            }
            return max;
        }
        
    }
};
