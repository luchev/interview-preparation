/**
 * Complexity (n = nodes in the list)
 * Time complexity: O(n)
 * Space complexity: O(1)
 */

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func swapNodes(head *ListNode, k int) *ListNode {
    if head == nil {
        return head
    }
    
    left := head
    for i := 1; i < k; i += 1 {
        if left != nil {
            left = left.Next
        }
    }
    if left == nil {
        return head
    }
    
    fast := left
    right := head
    for fast.Next != nil {
        fast = fast.Next
        right = right.Next
    }
    
    left.Val, right.Val = right.Val, left.Val
    
    return head
}