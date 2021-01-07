/**
 * Complexity (n = number of points)
 * Time complexity: O(n^2 * log(n))
 * Space complexity: O(n^2
 */
struct Point {
    int index;
    int length;
    Point(int i, int len) : index(i), length(len) { }
    
    bool operator<(const Point& rhs) const {
        return this->length > rhs.length;
    }
};

class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int total = 0;
        vector<bool> visited(points.size(), false);
        priority_queue<Point> queue;
        int visitedCount = 0;
        if (points.size() >= 2) {
            queue.push(Point(0, 0));
            visitedCount += 1;
        }
        
        while (visitedCount <= points.size() && !queue.empty()) {
            auto current = queue.top();
            queue.pop();
            if (visited[current.index]) {
                continue;
            }
            
            visited[current.index] = true;
            total += current.length;
            visitedCount++;
            
            for (int i = 0; i < points.size(); i++) {
                if (!visited[i]) {
                    queue.push(Point(i, abs(points[i][0] - points[current.index][0]) + abs(points[i][1] - points[current.index][1])));
                }
            }
        }
        
        
        return total;
    }
};
