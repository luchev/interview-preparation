struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

/**
 * Complexity (n = nodes in tree)
 * Time complexity: O(n)
 * Space complexity: O(n)
 *
 * If the tree is balanced:
 * Complexity (n = nodes in tree)
 * Time complexity: O(log(n))
 * Space complexity: O(log(n))
*/
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (p == root) {
            return p;
        }
        if (q == root) {
            return q;
        }
        
        if ((p->val > root->val && q->val < root->val) || (p->val < root->val && q->val > root->val)) {
            return root;
        }
        
        if (root->val > p->val && root->val > q->val) {
            return lowestCommonAncestor(root->left, p, q);
        }
        
         if (root->val < p->val && root->val < q->val) {
            return lowestCommonAncestor(root->right, p, q);
        }
        
        return nullptr;
        
    }
};