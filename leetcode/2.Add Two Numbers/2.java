/**
 * Complexity (n = max(size of list1, size of list2)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
class Solution {
    class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
        }
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode p1 = l1;
        ListNode p2 = l2;
        ListNode result = new ListNode(0);
        ListNode pRes = result;
        int carry = 0;
        boolean initializeList = true;
        while (p1 != null || p2 != null) {
            int a = p1 != null ? p1.val : 0;
            int b = p2 != null ? p2.val : 0;
            
            int sum = a + b + carry;
            if (initializeList) {
                pRes.val = sum % 10;
                initializeList = false;
            } else {
                pRes.next = new ListNode(sum % 10);
                pRes = pRes.next;
            }
            
            carry = sum > 9 ? 1 : 0;
            p1 = p1 != null ? p1.next : null;
            p2 = p2 != null ? p2.next : null;
        }
        
        if (carry > 0) {
            pRes.next = new ListNode(carry);
        }
        
        return result;
    }
}
