"""
Problem 2 - Queue using Stacks

We are given a stack data structure that supports standard operations like (push, pop, peek, and empty), implement a queue using instances of stack data structure and operations on them.

Implement a Queue class with the following methods:

    void push(int x): Pushes element x to the back of the queue.
    int pop(): Removes the element from the front of the queue and returns it.
    int peek(): Returns the element at the front of the queue.
    boolean empty(): Returns true if the queue is empty, false otherwise.

Example:

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

UMPIRE
Understand what the interviewer is asking for by using test cases and questions about the problem.
Match what this problem looks like to known categories of problems, e.g. Linked List or Dynamic Programming and strategies or patterns in those categories.
Plan the solution with appropriate visualizations and pseudocode.
Implement the code to solve the algorithm.
Review the code by running specific example(s) and recording values (watchlist) of your code's variables along the way.
Evaluate the performance of your algorithm and state any strong/weak or future potential work.

U:
    b: can we pop at 0? two stacks? (pop from one and pop from the other)
    k: can we use another data structure to implement a queue
    f: using a stack, but can we use a queue too? pop from both sides? (b)pop from the end
    t: agree with all
    x: CANADA 
    j: driver
    
M: 
    stack obviously
P:
    implement an enqueue method first
    - adding to the top of the stack
    pop:
    - move all elements except the first element from the main stack into fake stack 
    - return and delete 
    peek:
    - move all elements and return the first element
    empty:
    - if stack
I:
R:
E:
"""

if __name__ == "__main__":
    pass
