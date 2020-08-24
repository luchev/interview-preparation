# Complexity(n = number of nodes in the tree)
# Time complexity: O(n)
# Space complexity: O(n)


# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
def has_cycle(head):
    visited = set()
    pointer = head
    while pointer is not None:
        if pointer in visited:
            return True
        visited.add(pointer)
        pointer = pointer.next
    return False
