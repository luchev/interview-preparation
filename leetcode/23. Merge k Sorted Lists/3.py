# Complexity (n = number of lists, m = total number of items in all lists)
# Time complexity: O( m * log n )
# Space complexity: O(1)
# In reality it's slower than the array solution, but this solution doesn't use extra memory

import queue
# Define custom node to use the comparison operator in the priority queue
class CustomNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    # ListNode can be CustomNode
    def mergeKLists(self, lists: List[ListNode]) -> CustomNode:
        merged = CustomNode()
        pointer = merged

        que = queue.PriorityQueue()
        for list_ in lists:
            if list_ is not None:
                # Custom nodes .next points to ListNode so we have to convert in the while loop below 
                que.put(CustomNode(list_.val, list_.next))

        while not que.empty():
            head = que.get()
            pointer.next = head
            pointer = pointer.next

            head = head.next
            pointer.next = None

            if head is not None:
                que.put(CustomNode(head.val, head.next))

        return merged.next
