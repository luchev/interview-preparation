/**
 * Complexity (n = input array size, k = number of closest points to pick)
 * Time complexity: O(k * log(n))
 * Space complexity: O(n)
 */

#include <bits/stdc++.h>
using namespace std;

struct Point {
    int x;
    int y;

    bool operator<(const Point& rhs) const {
        return x * x + y * y > rhs.x * rhs.x + rhs.y * rhs.y;
    }
};

class Solution {
   public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        vector<Point> ps;
        for (auto x : points) {
            ps.push_back({x[0], x[1]});
        }

        std::make_heap(ps.begin(), ps.end());

        vector<vector<int>> result;
        for (int i = 0; i < K; i++) {
            std::pop_heap(ps.begin(), ps.end());
            vector<int> point;
            point.push_back(ps.rbegin()->x);
            point.push_back(ps.rbegin()->y);
            result.push_back(point);
            ps.pop_back();
        }

        return result;
    }
};
