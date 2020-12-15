/**
 * Complexity (n = items in list A, m = items in list B)
 * Time complexity: O(n + m)
 * Space complexity: O(n)
 */

 /*
    Find merge point of two linked lists
    Note that the head may be 'null' for the empty list.
    Node is defined as
    var Node = function(data) {
        this.data = data;
        this.next = null;
    }
*/
function findMergeNode( headA, headB ) {
    let pointerA = headA;
    while ( pointerA ) {
        pointerA.visited = true;
        pointerA = pointerA.next;
    }
    let pointerB = headB;
    while ( pointerB ) {
        if ( pointerB.visited ) {
            return pointerB.data;
        }
        pointerB = pointerB.next;
    }
    return null;
}
