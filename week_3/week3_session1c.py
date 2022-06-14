"""
Problem #3: Merge Two Sorted Lists
Merge two sorted linked lists.

Examples:

Input: 1->2->4, 1->3->4  
Output: 1->1->2->3->4->4

UMPIRE  
Understand what the interviewer is asking for by using test cases and questions about the problem.  
Match what this problem looks like to known categories of problems, e.g. Linked List or Dynamic Programming and strategies or patterns in those categories.  
Plan the solution with appropriate visualizations and pseudocode.  
Implement the code to solve the algorithm.  
Review the code by running specific example(s) and recording values (watchlist) of your code's variables along the way.  
Evaluate the performance of your algorithm and state any strong/weak or future potential work.  

U:
    bao:any order specific order to merge?
        duplicates allowed? yes :)
        how to handle duplicates?
        
    far: do we care about the length of the list? (same, different length)
    jes: driver hehe
    kev: what happens if we're given one empty list?
    tin: agree :)
    xin: merge in descending or ascending
        is there a cycle?
M:
    dummy node -> merged list
    two pointers -> pointer in each list and decide what will be added to the merged list next
    if not duplicates: set

P:
    - cases:
    if one current node == None
    check which one is less than the other one
    - the plannnn
    initialize two pointers:
    initialize a dummy node pointing to nothing
    while loop both are not none?
I:
R:
E:
"""


if __name__ == "__main__":
    pass
