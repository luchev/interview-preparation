/**
 * Complexity (n = items in the list)
 * Time complexity: O(n)
 * Space complexity: O(1)
 */

/*
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 */
function insertNodeAtPosition( head, data, position ) {
    if ( position === 0 ) {
        return {
            data: data,
            next: head,
        }
    }
    let pointer = head;
    while ( position > 1 ) {
        position--;
        pointer = pointer.next;
    }
    let newNode = {
        data: data,
        next: pointer.next,
    }
    pointer.next = newNode;

    return head;
}
