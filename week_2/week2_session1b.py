import random

"""
Problem 2 (Challenge) - Longest Consecutive Subsequence
Given an unsorted array of integers, we want to find
the length of the longest subsequence such that elements 
in the subsequence are consecutive integers. The consecutive 
numbers can be in any order.
Examples:
Input: [1, 9, 3, 10, 4, 20 , 2]
Output: 4
[1, 3, 4, 2] is the longest subsequence of consecutive elements.
"""

"""
UMPIRE  
Understand what the interviewer is asking for by using test cases and questions about the problem.  
Match what this problem looks like to known categories of problems, e.g. Linked List or Dynamic Programming and strategies or patterns in those categories.  
Plan the solution with appropriate visualizations and pseudocode.  
Implement the code to solve the algorithm.  
Review the code by running specific example(s) and recording values (watchlist) of your code's variables along the way.  
Evaluate the performance of your algorithm and state any strong/weak or future potential work.  

U:
-Are there going to be any duplicates on the list?
-What if we cannot find any consecutive, what if the list os empty?
-What if we have 2 subsequences of the same length?
-What is the maximum space complexity? 
-What is the max input list length?
-What is the time complexity expectations, linear?

M:
-Hash table
-make a set to remove the duplicates if there are any.

P:
-Create the hash table
-Loop through the list and add the values to be the key and the value to be the current number
-check if the current value is the 
"""

"""
U: Same as group above.
M: Same as group above.
P:
    1) Check early exit conditions: array length is 0 or 1
    2) Sort array
    3) Iterate through array and determine if current value is incremented compared to previous
        a) If so, add to current counter
        b) If not, compare max with current and reset current to 1(starting a new streak)
    4) Return with max streak count
I: See code below
R: Test cases are in main function
E: 
    Time: O(n*logN) because of the sort prior to processing
    Space: O(1) because only the current and max count are stored
"""


def kevc_solution(array: list):
    if len(array) == 0:
        return 0

    if len(array) == 1:
        return 1

    array.sort()
    longest = 0
    current = 0

    for idx, value in enumerate(array):
        if value == array[idx - 1]:
            continue

        if (value - array[idx - 1]) == 1:
            current += 1

        else:
            longest = max(longest, current)
            current = 1

    return max(longest, current)


if __name__ == "__main__":
    test_cases = [
        [1, 9, 3, 10, 4, 20, 2],
        [36, 41, 56, 35, 44, 33, 34, 43, 92, 32, 42],
        [3],
        [],
        [3, 9, 50, 2, 8, 4, 1],
        [1, 5, 29, 4, 3, 2, 1],
        [random.randint(1, 10) for _ in range(10)],
    ]
    for idx, array in enumerate(test_cases, start=1):
        print(f"Test case {idx}: {sorted(array)}")
        print(f"Longest subsequence: {kevc_solution(array)}")
