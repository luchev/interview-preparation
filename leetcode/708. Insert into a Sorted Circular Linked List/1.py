# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: Node, insertVal: int) -> Node:
        if head is None:
            head = Node(insertVal)
            head.next = head
            return head

        pointer = head
        end = head
        while not pointer.val <= insertVal <= pointer.next.val:
            if pointer.val <= pointer.next.val > pointer.next.next.val:
                end = pointer.next

            pointer = pointer.next
            if pointer == head:
                pointer = end
                break

        pointer.next = Node(insertVal, pointer.next)

        return head
