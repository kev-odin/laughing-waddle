"""
Problem #3: Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example:
Input: 2 -> 4 -> 3,  5 -> 6 -> 4
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807
UMPIRE  
Understand what the interviewer is asking for by using test cases and questions about the problem.  
Match what this problem looks like to known categories of problems, e.g. Linked List or Dynamic Programming and strategies or patterns in those categories.  
Plan the solution with appropriate visualizations and pseudocode.  
Implement the code to solve the algorithm.  
Review the code by running specific example(s) and recording values (watchlist) of your code's variables along the way.  
Evaluate the performance of your algorithm and state any strong/weak or future potential work.
U: 
    bao:Can the output list be longer the input list? Should we make a new node for the last carry over or should we 
    trash it?
    far:
    jes:Is there a possibility of an empty list?
    -What will happen if there is a carry over for every digit?
    kev:What if the length of the lists are not the same? 
    tin:
    xin:
M:
-Linked list!!
-two pointers
-dummy nodes to store the sum of the two lists
-multiple passes to get the lengths? maybe

P: 
Create a dummy node to point to the head
initiate the two pointers to point to the head of the lists
create a current node 
initiate a variable to store the carry over value
Traverse the two lists while the pointers are not null
  -get the sum of each two pointer values
  -get the carry over values
  -if there is a carry over connect it to the end of the list
 return dummy.next


I:
R:
E: 
time complexity : O(M + N)
space complexity: O(N + 1) = O(N)  - N being longest list length 
"""
