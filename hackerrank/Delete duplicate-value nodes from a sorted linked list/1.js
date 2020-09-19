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
function removeDuplicates( head ) {
    let pointer = head;
    while ( pointer ) {
        if ( !pointer.next ) {
            break;
        }
        if ( pointer.data === pointer.next.data ) {
            pointer.next = pointer.next.next;
        } else {
            pointer = pointer.next;
        }
    }
    return head;
}
