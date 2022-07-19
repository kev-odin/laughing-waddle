"""Write a method that takes an integer as input and returns its string representation.

Examples:

Input: 123
Output: "123"

Input: -6714
Ouput: "-6714"

UMPIRE
Understand what the interviewer is asking for by using test cases and questions about the problem.
Match what this problem looks like to known categories of problems, e.g. Linked List or Dynamic Programming and strategies or patterns in those categories.
Plan the solution with appropriate visualizations and pseudocode.
Implement the code to solve the algorithm.
Review the code by running specific example(s) and recording values (watchlist) of your code's variables along the way.
Evaluate the performance of your algorithm and state any strong/weak or future potential work.
U:
    bao: Can we use cast in this problem? 
    far: Does it come with any special characters or signs?
    jes: Is there a decimal number?
    kev: Do we need to worry about the sign of integer?
    tin: Negative number, what should we return? (driver)
    xin: Leading 0, is that a valid input?
M:
    while loop, math(module), deque
P:  
    integer -> string
    create a deque
    assign negative sign to False
    check if num input is less than 0:
        negative sign is True
        convert negative to positive by multiply (-1)
    while input greater than 0:
        get the last digit by modulus by 10
        get the rest of digit by divide by 10
        convert integer to string and add to deque
    check if there is a negative sign:
        if so, add to the left of the deque
    return join(num_deque)
I: **see below**
R:
E: Time: O(N)
   Space: O(N)
"""
from collections import deque

def solution(num: int) -> str:
    num_deque = deque()
    negative = False
    
    if num < 0:
        negative = True
        num = num * (-1) 
        
    while num > 0:
        lastdigit = num % 10
        num = num // 10
        num_deque.appendleft(chr(ord('0') + lastdigit))
        
    if negative:
        num_deque.appendleft("-")
        
    return "".join(num_deque)
  
if __name__ == "__main__":
    print(solution(123))  # output: 123
    print(solution(-6714)) # ouput: -6714
    print(type(solution(6714))) # output: str
