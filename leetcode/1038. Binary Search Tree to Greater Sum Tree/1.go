/**
 * Complexity (n = nodes in the tree)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func bstToGst(root *TreeNode) *TreeNode {
	dfs(root, 0)
	return root
}

func dfs(root *TreeNode, total int) int {
	if root == nil {
		return total
	}
	rightSum := dfs(root.Right, total)
	rightAndRootSum := rightSum + root.Val
	root.Val += rightSum
	leftSum := dfs(root.Left, rightAndRootSum)
	return leftSum
}
