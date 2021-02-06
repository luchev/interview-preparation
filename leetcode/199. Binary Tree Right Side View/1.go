/**
 * Complexity (n = nodes in the tree)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rightSideView(root *TreeNode) []int {
	var rightSide []int = nil
	dfs(root, 1, &rightSide)
	return rightSide
}

func dfs(root *TreeNode, depth int, rightSide *[]int) {
	if root == nil {
		return
	}
	if depth > len(*rightSide) {
		(*rightSide) = append(*rightSide, root.Val)
	}
	dfs(root.Right, depth+1, rightSide)
	dfs(root.Left, depth+1, rightSide)
}
