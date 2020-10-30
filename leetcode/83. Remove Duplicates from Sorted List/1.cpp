/**
 * Complexity (n = input linked list size)
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
   public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head) {
            return head;  // nullptr
        }

        ListNode* newHead = new ListNode(head->val);
        ListNode* tail = newHead;
        while (head) {
            if (head->val != tail->val) {
                tail->next = new ListNode(head->val);
                tail = tail->next;
            }
            head = head->next;
        }

        return newHead;
    }
};
