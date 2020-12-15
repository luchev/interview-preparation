#include <bits/stdc++.h>
using namespace std;

/**
 * Complexity (n = number of nodes, m = number of edges)
 * Time complexity: O(m * logn)
 * Space complexity: O(n + m)
 */
struct Pair {
    int index;
    int distance;
};

struct Node {
    list<Pair> neighbours;

    bool hasNeighbour(int index) {
        for (auto neighbour : neighbours) {
            if (neighbour.index == index) {
                return true;
            }
        }
        return false;
    }

    void addNeighbour(int index, int distance) {
        neighbours.push_back(Pair{index, distance});
    }
};

struct Edge {
    int from;
    int to;
    int distance;

    bool operator<(const Edge &rhs) const {
        return distance > rhs.distance;
    }
};

class Graph {
   private:
    vector<Node> nodes;

   public:
    Graph(int nodeCount = 0) {
        nodes.resize(nodeCount);
    }

    void print() const {
        for (int node = 0; node < nodes.size(); node++) {
            cout << node << ": ";
            for (auto neighbour : nodes[node].neighbours) {
                cout << neighbour.index << "(" << neighbour.distance << "), ";
            }
            cout << "\n";
        }
    }

    void connect(int from, int to, int distance) {
        nodes[from].addNeighbour(to, distance);
        nodes[to].addNeighbour(from, distance);
    }

    vector<Edge> getAllEdges() const {
        vector<Edge> edges;

        for (int from = 0; from < nodes.size(); from++) {
            for (auto neighbour : nodes[from].neighbours) {
                int to = neighbour.index;
                int distance = neighbour.distance;
                if (from < to) {
                    edges.push_back(Edge{from, to, distance});
                }
            }
        }

        return edges;
    }

    int prim(int start) const {
        if (nodes.size() < 1) {
            return 0;
        }
        vector<int> distance(nodes.size(), INT_MAX);
        vector<bool> added(nodes.size(), false);

        distance[start] = 0;
        priority_queue<Edge> nextToProcess;
        nextToProcess.push({-1, start, 0});  // start from the 0th node with no parent

        int totalWeight = 0;
        while (!nextToProcess.empty()) {
            Edge nextBest = nextToProcess.top();
            nextToProcess.pop();
            int currentNode = nextBest.to;

            if (added[currentNode]) {
                continue;
            }
            added[currentNode] = true;

            int minDistance = nextBest.distance;
            cout << "Add " << currentNode << " with dist " << minDistance << "\n";
            totalWeight += minDistance;

            for (auto neighbour : nodes[currentNode].neighbours) {
                cout << "Add neighbour " << neighbour.index << " ( " << neighbour.distance << " )\n";
                nextToProcess.push({currentNode, neighbour.index, neighbour.distance});
            }
        }

        return totalWeight;
    }
};

int prims(int n, vector<vector<int>> edges, int start) {
    Graph g(n + 1);
    for (auto i : edges) {
        g.connect(i[0], i[1], i[2]);
    }
    return g.prim(start);
}

vector<string> split_string(string);

int main() {
    ofstream fout(getenv("OUTPUT_PATH"));

    string nm_temp;
    getline(cin, nm_temp);

    vector<string> nm = split_string(nm_temp);

    int n = stoi(nm[0]);

    int m = stoi(nm[1]);

    vector<vector<int>> edges(m);
    for (int i = 0; i < m; i++) {
        edges[i].resize(3);

        for (int j = 0; j < 3; j++) {
            cin >> edges[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    int start;
    cin >> start;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int result = prims(n, edges, start);

    fout << result << "\n";

    fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [](const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
