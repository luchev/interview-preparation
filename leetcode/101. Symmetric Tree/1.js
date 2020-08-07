/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
/**
 * Complexity (n = input length)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
var isSymmetric = function ( root ) {
    if ( !root ) {
        return true;
    }
    return checkSymmetry( root.left, root.right );
};

function checkSymmetry( left, right ) {
    if ( !left && !right ) {
        return true;
    } else if ( left && right && left.val === right.val ) {
        return checkSymmetry( left.right, right.left ) && checkSymmetry( left.left, right.right );
    }
    return false;
}
