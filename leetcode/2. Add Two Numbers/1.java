/**
 * Complexity (n = max(size of list1, size of list2))
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
        while (p1 != null && p2 != null) {
            int sum = p1.val + p2.val + carry;
            if (p1 == l1) {
                pRes.val = sum % 10;
            } else {
                pRes.next = new ListNode(sum % 10);
                pRes = pRes.next;
            }

            carry = sum / 10;
            p1 = p1.next;
            p2 = p2.next;
        }

        while (p1 != null) {
            int sum = p1.val + carry;
            if (p1 == l1) {
                pRes.val = sum % 10;
            } else {
                pRes.next = new ListNode(sum % 10);
                pRes = pRes.next;
            }

            carry = sum / 10;
            p1 = p1.next;
        }

        while (p2 != null) {
            int sum = p2.val + carry;
            if (p2 == l2) {
                pRes.val = sum % 10;
            } else {
                pRes.next = new ListNode(sum % 10);
                pRes = pRes.next;
            }

            carry = sum / 10;
            p2 = p2.next;
        }

        if (carry > 0) {
            pRes.next = new ListNode(carry);
        }

        return result;
    }
}
