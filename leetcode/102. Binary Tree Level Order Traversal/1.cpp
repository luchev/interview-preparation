#include <bits/stdc++.h>
using namespace std;
/**
 * Complexity (n = nodes in the tree)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
   public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> levels = vector<vector<int>>(1);

        queue<TreeNode*> frontier;
        if (root) {
            frontier.push(root);
        }

        queue<TreeNode*> next_frontier;

        while (!frontier.empty()) {
            TreeNode* curr = frontier.front();
            frontier.pop();
            levels[levels.size() - 1].push_back(curr->val);

            if (curr->left) {
                next_frontier.push(curr->left);
            }
            if (curr->right) {
                next_frontier.push(curr->right);
            }

            if (frontier.empty()) {
                frontier = queue<TreeNode*>(move(next_frontier));
                next_frontier = queue<TreeNode*>();
                levels.push_back(vector<int>());
            }
        }
        levels.pop_back();
        return levels;
    }
};
