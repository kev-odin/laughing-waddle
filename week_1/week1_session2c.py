"""
Problem #3 Pow(x,n)
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Examples:

Input: x = 2.00000, n = 10
Output: 1024.00000

Input: x = 2.10000, n = 3
Output: 9.26100

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""

"""
Understand what the interviewer is asking for by using test cases and questions about the problem.  
Match what this problem looks like to known categories of problems, e.g. Linked List or Dynamic Programming and strategies or patterns in those categories.  
Plan the solution with appropriate visualizations and pseudocode.  
Implement the code to solve the algorithm.  
Review the code by running specific example(s) and recording values (watchlist) of your code's variables along the way.  
Evaluate the performance of your algorithm and state any strong/weak or future potential work.  
"""

"""
U: Replicate the result of the inbuilt power function
M: Recursion, simple math
P: Base case - n is 0 = 1 OR x is 0; recursive case n is something other than 0
I: See below
R: Test cases are in main function
E: 
Time complexity O(n) because we have to decrement the value of n until we reach our base case.
Space complexity O(n) because we are using the call stack to hold our values before pop out of our recursive calls.
"""


def kevc_solution(x: int, n: int):
    if x == 0:
        return 0
    if n == 0:
        return 1
    elif n > 0:
        return x * kevc_solution(x, n - 1)
    else:
        return 1 / x * kevc_solution(x, n + 1)


if __name__ == "__main__":
    test = [(2, 10), (2.1, 3), (2, -2)]
    for val in test:
        print(kevc_solution(*val))
