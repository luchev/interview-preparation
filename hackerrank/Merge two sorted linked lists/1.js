/**
 * Complexity (n = items in list 1, m = items in list 2)
 * Time complexity: O(n + m)
 * Space complexity: O(n + m)
 */

/*
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 */
function mergeLists( head1, head2 ) {
    let merged = {data: 0, next: null};
    let pointer1 = head1;
    let pointer2 = head2;
    let mergedPointer = merged;

    while ( pointer1 && pointer2 ) {
        if ( pointer1.data <= pointer2.data ) {
            mergedPointer.next = {
                data: pointer1.data,
            }
            pointer1 = pointer1.next;
        } else {
            mergedPointer.next = {
                data: pointer2.data,
            }
            pointer2 = pointer2.next;
        }
        mergedPointer = mergedPointer.next
        console.log( mergedPointer );
        mergedPointer.next = null;
    }

    while ( pointer1 ) {
        mergedPointer.next = {
            data: pointer1.data
        }
        pointer1 = pointer1.next;
        mergedPointer = mergedPointer.next;
        mergedPointer.next = null;
    }

    while ( pointer2 ) {
        mergedPointer.next = {
            data: pointer2.data
        }
        pointer2 = pointer2.next;
        mergedPointer = mergedPointer.next;
        mergedPointer.next = null;
    }


    return merged.next;
}
