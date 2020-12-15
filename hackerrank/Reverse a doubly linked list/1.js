/**
 * Complexity (n = items in the list)
 * Time complexity: O(n)
 * Space complexity: O(1)
 */

/*
 * DoublyLinkedListNode {
 *     int data;
 *     DoublyLinkedListNode next;
 *     DoublyLinkedListNode prev;
 * }
 */
function reverse( head ) {
    let pointer = head;
    let next = null;
    while ( pointer ) {
        next = pointer.next;
        pointer.next = pointer.prev;
        pointer.prev = next;
        if ( !next ) {
            return pointer;
        }
        pointer = next;
    }
    return head;

}
