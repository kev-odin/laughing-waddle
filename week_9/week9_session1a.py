"""
Problem 1: Stack using Queues

Given a Queue data structure that supports standard operations like push, top, pop, and empty. 
Implement a Stack data structure using only instances of Queue and queue operations allowed on the instances.

Implement a Stack class:

    void push(int x): Pushes element x to the top of the stack.
    int pop(): Removes the element on the top of the stack and returns it.
    int top(): Returns the element on the top of the stack.
    boolean empty(): Returns true if the stack is empty, false otherwise.

Example:
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

2:46PM - 3:01PM

Understanding:
Implement a Stack based on Queue 
Only return when top or pop
return T or F when empty is called
not returning anything when push
1, 2

Match:
deque -> double ended queue

Plan:
Initialize a Stack class
Intilize a queue as deque inside of Stack
Implement the push function by using appending the value to the queue
Implement the empty function by checking if the queue is empty or not
Implement the pop function by dequeuing all the elements in the initial queue to the auxillary queue except
of the last element. Then deque and return the last element.
Implement the top function by dequeing all the elements in the initial queue to the auxillary queue except
of the last element. Then store the last element and then dequue to the aux queue and return the stored element afterward
I would make the current queue to be the aux_queue then make new aux_queue

queue =  
aux_queue = 1, 2
queue = aux_queue
aux_queue = []

Implement:
Review:


"""
from collections import deque
class Stack():
    def __init__(self):
        self.queue = deque()
        self.aux_queue = deque()
        
    def push(self, val):
        self.queue.append(val)
        
    def empty(self):
        if self.queue:
            return True
        else:
            return False
            
    def pop(self, val):
        while len(self.queue) >= 1:
            self.aux_queue.append(self.queue.popleft())
        topStack = self.queue.popleft()
        queue = aux_queue
        aux_queue = deque()
        return topStack

    def top(self, val):
        while len(self.queue) >= 1:
            self.aux_queue.append(self.queue.popleft())
        topStack = self.queue.popleft()
        self.aux_queue.append(topStack)
        queue = aux_queue
        aux_queue = deque()
        return topStack
    
            
