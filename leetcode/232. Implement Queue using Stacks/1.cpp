/**
 * Complexity (n = number of queries)
 * Time complexity: O(n) for all queries
 * Space complexity: O(n) for all queries
 * Time complexity per operation: O(1) (amortized for pop() and peek())
 */

#include <stack>
using namespace std;
class MyQueue {
   public:
    stack<int> back;
    stack<int> front;

    /** Initialize your data structure here. */
    MyQueue() {
    }

    /** Push element x to the back of queue. */
    void push(int x) {
        back.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if (front.empty()) {
            transfer();
        }
        int top = front.top();
        front.pop();
        return top;
    }

    /** Get the front element. */
    int peek() {
        if (front.empty()) {
            transfer();
        }
        return front.top();
    }

    void transfer() {
        while (!back.empty()) {
            front.push(back.top());
            back.pop();
        }
    }

    /** Returns whether the queue is empty. */
    bool empty() {
        return back.empty() && front.empty();
    }
};
