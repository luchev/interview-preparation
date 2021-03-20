/**
 * Complexity (n = input string length)
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
func str2tree(s string) *TreeNode {
	if len(s) == 0 {
		return nil
	}
	tokens := split(s)

	var parents []*TreeNode
	parents = append(parents, &TreeNode{0, nil, nil})
	for _, token := range tokens {
		if token == "(" {
			if parents[len(parents)-1].Left == nil {
				parents[len(parents)-1].Left = &TreeNode{0, nil, nil}
				parents = append(parents, parents[len(parents)-1].Left)
			} else {
				parents[len(parents)-1].Right = &TreeNode{0, nil, nil}
				parents = append(parents, parents[len(parents)-1].Right)
			}
		} else if token == ")" {
			parents = parents[:len(parents)-1]
		} else {
			convertedInt, _ := strconv.ParseInt(token, 10, 32)
			parents[len(parents)-1].Val = int(convertedInt)
		}
	}

	return parents[0]
}

func split(s string) []string {
	var parts []string
	var buffer []rune

	for _, char := range s {
		if char == '(' || char == ')' {
			if len(buffer) > 0 {
				parts = append(parts, string(buffer))
				buffer = nil
			}
			parts = append(parts, string(char))
		} else {
			buffer = append(buffer, char)
		}
	}

	if len(buffer) > 0 {
		parts = append(parts, string(buffer))
		buffer = nil
	}

	return parts
}
