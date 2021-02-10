/**
 * Complexity (n = nodes in the linked list)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */

/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
	nodes := make(map[*Node]*Node)
	newHead := Node{0, nil, nil}
	newPtr := &newHead

	headPtr := head
	for headPtr != nil {
		newPtr.Next = &Node{headPtr.Val, nil, nil}
		nodes[headPtr] = newPtr.Next

		headPtr = headPtr.Next
		newPtr = newPtr.Next
	}

	newPtr = &newHead
	headPtr = head
	for headPtr != nil {
		newPtr.Next.Random = nodes[headPtr.Random]

		headPtr = headPtr.Next
		newPtr = newPtr.Next
	}

	return newHead.Next
}
