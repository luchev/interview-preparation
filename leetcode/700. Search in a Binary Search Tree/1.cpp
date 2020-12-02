/**
 * Complexity (n = nodes in the tree)
 * Time complexity: O(n)
 * Space complexity: O(n) or O(1) if the recursion is converted to tail recursion
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
    TreeNode* searchBST(TreeNode* root, int val) {
        if (!root) {
            return nullptr;
        }
        if (root->val == val) {
            return root;
        } else if (val < root->val) {
            return searchBST(root->left, val);
        } else {
            return searchBST(root->right, val);
        }
    }
};
