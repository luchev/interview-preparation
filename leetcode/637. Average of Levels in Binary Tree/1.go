/**
 * Complexity (n = nodes in the graph)
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
func averageOfLevels(root *TreeNode) []float64 {
    accumulator := make([]float64, 0)
    counts := make([]float64, 0)
    dfs(root, &accumulator, &counts, 0)
    
    for i, _ := range accumulator {
        accumulator[i] /= counts[i]
    }
    
    return accumulator
}

func dfs(root *TreeNode, accumulator *[]float64, counts *[]float64, currentLevel int) {
    if root != nil {
        if len(*accumulator) <= currentLevel {
            *accumulator = append(*accumulator, 0)
            *counts = append(*counts, 0)
        }
        
        (*accumulator)[currentLevel] += float64(root.Val)
        (*counts)[currentLevel] += 1
        
        dfs(root.Left, accumulator, counts, currentLevel + 1)
        dfs(root.Right, accumulator, counts, currentLevel + 1)
    }
}
