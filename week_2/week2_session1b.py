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

if __name__ == "__main__":
    pass
