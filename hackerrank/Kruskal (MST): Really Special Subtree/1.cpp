/**
 * Complexity (m = edges in the graph)
 * Time complexity: O(m * log(m))
 * Space complexity: O(m)
 */

#include <bits/stdc++.h>
using namespace std;
string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

struct Edge {
    int from;
    int to;
    int weight;
    
    bool operator<(const Edge& rhs) const {
        return weight > rhs.weight;
    }
};

int kruskals(int g_nodes, vector<int> g_from, vector<int> g_to, vector<int> g_weight) {
    vector<Edge> edges;
    for (size_t i = 0; i < g_from.size(); i++) {
        edges.push_back({g_from[i], g_to[i], g_weight[i]});
    }
    
    sort(edges.begin(), edges.end());
    vector<int> components(g_nodes + 1);
    for (size_t i = 0; i < components.size(); i++) {
        components[i] = i;
    }
    
    int edgeCount = 0;
    int weight = 0;
    while (edgeCount != g_nodes - 1) {
        auto edge = *edges.rbegin();
        edges.pop_back();
        if (components[edge.from] != components[edge.to]) {
            edgeCount++;
            weight += edge.weight;
            int oldComponent = components[edge.from];
            int newComponent = components[edge.to];
            for (size_t i = 0; i < components.size(); i++) {
                if (components[i] == oldComponent) {
                    components[i] = newComponent;
                }
            }
        }
    }
    
    return weight;
    
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string g_nodes_edges_temp;
    getline(cin, g_nodes_edges_temp);

    vector<string> g_nodes_edges = split(rtrim(g_nodes_edges_temp));

    int g_nodes = stoi(g_nodes_edges[0]);
    int g_edges = stoi(g_nodes_edges[1]);

    vector<int> g_from(g_edges);
    vector<int> g_to(g_edges);
    vector<int> g_weight(g_edges);

    for (int i = 0; i < g_edges; i++) {
        string g_from_to_weight_temp;
        getline(cin, g_from_to_weight_temp);

        vector<string> g_from_to_weight = split(rtrim(g_from_to_weight_temp));

        int g_from_temp = stoi(g_from_to_weight[0]);
        int g_to_temp = stoi(g_from_to_weight[1]);
        int g_weight_temp = stoi(g_from_to_weight[2]);

        g_from[i] = g_from_temp;
        g_to[i] = g_to_temp;
        g_weight[i] = g_weight_temp;
    }

    int res = kruskals(g_nodes, g_from, g_to, g_weight);

    fout << res;

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
