"""
Problem 1: Remove Nth Node from End of List
Given a linked list, remove the n-th node from the end of list and return its head.
Example:
Input: 1->2->3->4->5, n = 2
Output: 1->2->3->5
Explanation: We remove the second node from the end, the node with value 4
UMPIRE  
Understand what the interviewer is asking for by using test cases and questions about the problem.  
Match what this problem looks like to known categories of problems, e.g. Linked List or Dynamic Programming and strategies or patterns in those categories.  
Plan the solution with appropriate visualizations and pseudocode.  
Implement the code to solve the algorithm.  
Review the code by running specific example(s) and recording values (watchlist) of your code's variables along the way.  
Evaluate the performance of your algorithm and state any strong/weak or future potential work.
U: 
    bao: is there a cycle?
        - are there constraints to n's value? negative values?
    far: is the list empty?
    jes:
    kev: what are we expected to return? - return the head :)
    tin: what if there are two same values? - remove both or just one?
        - position of the node from the last node
    xin: when n is greater than the length of the linked list, will it go backwards?
    
testcase:
- single node; n = 1, 0? bad inputs
- cycle one: 1 -> 2 -> 3 -> 4 -> 1 - no way to find the end 
-  1->2->3->4->5, n = 2, 5
M:
    assume: n will not be larger than the length of the list 
    two pointers -> fast and slow pointers, keep the distance between the fast and slow pointer to be n
    - moving in the same speed? - moving the same speed, fast: will have distance, distance will be n
    - two passes: getting the length of the list (length - n +/- 1), finding the need to delete value: two pointers
    - dummy node?
    - 
P: 
make two pointers:
make dummy node pointing to head?
for loop in range of n:
    update fastpointer 
    if fastpointer == null:
       return dummyheadnode.next
       
while loop to move fastpointer.next is not null:
    update slowpointer, fastpointer
make slowpointer.next equal the next next value

return the dummyheadnode :)



I:
R:
E: 
time complex: O(n)
space complex: O(1)?
"""
