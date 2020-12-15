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
function printLinkedList( head ) {
    let pointer = head;
    while ( pointer ) {
        console.log( pointer.data );
        pointer = pointer.next;
    }

}
