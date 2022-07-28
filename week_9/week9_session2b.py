"""
Problem #2: Score of Parentheses

Given a balanced parentheses string S, compute the score of the string based on the following rule:

    () has score 1
    AB has score A + B, where A and B are balanced parentheses strings.
    (A) has score 2 * A, where A is a balanced parentheses string.

Examples:

Input: "()"
Output: 1

Input: "(())"
Output: 2

Input: "()()"
Output: 2

Input: "(()(()))" 2(1 + 2) = 6
Output: 6

U: 
    any whitespaces, special characters: nothing
    always will be open or close
    
M:
    stack
    math
P:
    intialize an array stack
    loop through the string of para:
        if "(" push 1 onto the stack
        else ):
            pop from the stack
            add to the total
I: see below
R
E: 
run time: O(N) 
space: O(N)
"""

def bal_para(s):
    stack = []
    total = 0

    for char in s:
        if char == '(':
            stack.append(1)
            
        elif char == ')':
            
            total += stack.pop(-1)
    return total
    
print(bal_para("(()(()))"))
            
    