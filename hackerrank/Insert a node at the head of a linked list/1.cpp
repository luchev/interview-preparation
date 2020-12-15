/**
 * Complexity (n = array length)
 * Time complexity: O(1)
 * Space complexity: O(n)
 */
struct SinglyLinkedListNode {
    int data;
    SinglyLinkedListNode* next;
};

SinglyLinkedListNode* insertNodeAtHead(SinglyLinkedListNode* llist, int data) {
    SinglyLinkedListNode* newHead = new SinglyLinkedListNode{data};
    newHead->next = llist;
    return newHead;
}
