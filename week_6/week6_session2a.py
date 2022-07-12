"""
Problem 1 - Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

    MovingAverage(int size): Initializes the object with the size of the window size.
    double next(int val): Returns the moving average of the last size values of the stream.

Examples

Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

UMPIRE
Understand what the interviewer is asking for by using test cases and questions about the problem.
Match what this problem looks like to known categories of problems, e.g. Linked List or Dynamic Programming and strategies or patterns in those categories.
Plan the solution with appropriate visualizations and pseudocode.
Implement the code to solve the algorithm.
Review the code by running specific example(s) and recording values (watchlist) of your code's variables along the way.
Evaluate the performance of your algorithm and state any strong/weak or future potential work.

U:
    bao: What if k is longer than the length of the output list?
    far: Empty list? Correct inputs? Is there a limit to the size of the input?
    jes: What is the cutoff for float value rounding decimals? | What about negative values?
    kev: Driving
    tin: What if k is equal to 1?
    xin: Moving to Canada
M:
    * Queue
    * Two pointers
    * Math (numbers and values)
P:
    * Append values into the queue until we reach the size
        Return the calculated average
    * When the size is reached. 
        Popleft, subtract value from the total, return average
I:
    * See below
R:
    * See below
E:
    * Time: O(1) becuase math. Implementation details supports this operation.
    * Space: O(1) because of input will not change the size of the structure.
        * Bao dissent: O(k)
"""
from collections import deque


class MovingAverage:
    def __init__(self, size=0):
        self.size = size
        self.total = 0
        self.q = deque()

    def next(self, val: int) -> float:
        self.q.append(val)

        if len(self.q) > self.size:
            self.total -= self.q.popleft()

        self.total += val

        return self.total / len(self.q)


if __name__ == "__main__":

    test = MovingAverage(3)
    print(test.next(1))
    # return 1.0 = 1 / 1
    print(test.next(-10))
    # return 5.5 = (1 + 10) / 2
    print(test.next(3))
    # return 4.66667 = (1 + 10 + 3) / 3
    print(test.next(5))
    # return 6.0 = (10 + 3 + 5) / 3
