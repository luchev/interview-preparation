/**
 * Complexity (n = number of items in the list)
 * Time complexity: O(n)
 * Space complexity: O(1)
 */

struct SinglyLinkedListNode {
    int data;
    SinglyLinkedListNode* next;
};

SinglyLinkedListNode* insertNodeAtTail(SinglyLinkedListNode* head, int data) {
    SinglyLinkedListNode* it = head;
    if (it == nullptr) {
        it = new SinglyLinkedListNode{data};
        return it;
    }

    SinglyLinkedListNode* HEAD = head;
    while (it->next != nullptr) {
        it = it->next;
    }

    it->next = new SinglyLinkedListNode{data};
    return HEAD;
}
