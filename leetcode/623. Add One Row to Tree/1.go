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
func addOneRow(root *TreeNode, v int, d int) *TreeNode {
	if d == 1 {
		return &TreeNode{v, root, nil}
	}
	dfs(root, v, d-1)
	return root
}

func dfs(root *TreeNode, value int, depth int) {
	if root == nil {
		return
	}

	if depth == 1 {
		root.Left = &TreeNode{value, root.Left, nil}
		root.Right = &TreeNode{value, nil, root.Right}
	} else {
		dfs(root.Left, value, depth-1)
		dfs(root.Right, value, depth-1)
	}
}
