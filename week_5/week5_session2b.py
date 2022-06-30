"""
Problem #2: Valid Parentheses
Given a string s containing characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Input: s = "()"
Output: true
Input: s = "(]"
Output: false
UMPIRE  
Understand what the interviewer is asking for by using test cases and questions about the problem.  
Match what this problem looks like to known categories of problems, e.g. Linked List or Dynamic Programming and strategies or patterns in those categories.  
Plan the solution with appropriate visualizations and pseudocode.  
Implement the code to solve the algorithm.  
Review the code by running specific example(s) and recording values (watchlist) of your code's variables along the way.  
Evaluate the performance of your algorithm and state any strong/weak or future potential work.
U: 
    bao: Driving :">
    far: What if there are special characters that are not brackets? Assume that the string will only contain three types of 
    brackets. Empty -> return True, input cannot be empty. There would be at least one bracket in the input.
    jes: Would there be white spaces between the brackets? Just brackets :)
    kev: agree
    tin: True for the example "()[]"
    xin: Would the length of the string be even? No, the length could either be odd or even
    ian: edge cases
)))((( -> false

M:
Stack

P: 
Create the Stack
Check if the length of the stack is odd -> return false
Push all the opening brackets into the stack 

I:
R:
E: 
"""

if __name__ == "__main__":
    pass