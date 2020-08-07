/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
/**
 * Complexity (n = number of nodes in tree)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
class Solution {
   public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        if (root == nullptr) {
            return result;
        }
        traverse(result, root);
        return result;
    }

    void traverse(vector<int>& result, TreeNode* root) {
        if (root->left) {
            traverse(result, root->left);
        }

        result.push_back(root->val);

        if (root->right) {
            traverse(result, root->right);
        }
    }
};
