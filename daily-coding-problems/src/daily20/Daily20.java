package daily20;

class Daily20 {
    /**
     * Find the node where 2 singly linked lists intersect
     * If such node is found - return its value, else return -1
     *
     * Complexity (n = list A size, k = list B size)
     * Time complexity: O(n + k)
     * Space complexity: O(1)
     *
     * @param a - linked list A
     * @param b - linked list B
     * @return - the value of the node where the 2 lists intersect, -1 if no intersection exists
     */
    static int getIntersection(LL<Integer> a, LL<Integer> b) {
        int aIndex = a.getSize();
        int bIndex = b.getSize();
        LLNode<Integer> bPointer = b.getRoot();
        // If there are more items in list b, skip the first few to have equal number of items from the current
        // pointers to the end of the list
        while (aIndex < bIndex) {
            bPointer = bPointer.getNext();
            bIndex--;
        }

        // If there are more items in list a, skip the first few to have equal number of items from the current
        // pointers to the end of the list
        LLNode<Integer> aPointer = a.getRoot();
        while (bIndex < aIndex) {
            aPointer = aPointer.getNext();
            aIndex--;
        }

        boolean equalStreak = false;
        LLNode<Integer> lastEqual = null;
        // Iterate all items and compare if the ith item from the back of list a is the same as the
        // ith item from the back of list a.
        // If the items are the same - possibly it's an equals streak
        // If the items are different - destroy any equal streaks if we had any
        while (aIndex > 0) {
            if (aPointer.getData().equals(bPointer.getData())) {
                if (!equalStreak) {
                    equalStreak = true;
                    lastEqual = aPointer;
                }
            } else {
                equalStreak = false;
                lastEqual = null;
            }

            // Move to the next item in the linked lists
            aIndex--;
            aPointer = aPointer.getNext();
            bPointer = bPointer.getNext();
        }

        // If we had any equal streaks we will keep the node where the streak started in lastEqual,
        // else we have no intersecting nodes -> return -1 as error
        if (lastEqual != null) {
            return lastEqual.getData();
        } else {
            return -1;
        }
    }
}
