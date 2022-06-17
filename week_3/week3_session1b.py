"""
Problem #2: Linked List Cycle
Given a linked list, determine if it has a cycle in it. For simplicity, assume the linked list cannot have more than 1000 nodes in it.

Examples:

This linked list would return True

Image of circular Linked List with values in order 3,2,0,4 and pointer from 4 to 2
    3 -> 2 -> 0 -> 4 -> 2
This linked list would return False

Image of single linked list with value of 1
    1

UMPIRE  
Understand what the interviewer is asking for by using test cases and questions about the problem.  
Match what this problem looks like to known categories of problems, e.g. Linked List or Dynamic Programming and strategies or patterns in those categories.  
Plan the solution with appropriate visualizations and pseudocode.  
Implement the code to solve the algorithm.  
Review the code by running specific example(s) and recording values (watchlist) of your code's variables along the way.  
Evaluate the performance of your algorithm and state any strong/weak or future potential work.  

U:
    bao: Are there None value in the middle of the list?
    far: Is it possible that the list is empty?
    jes: Are there only one cycle in the linkedlist? 
         would the value always be numbers/int?
         duplicated values?
    kev: Do we have any space requirements?
    tin: Agree
    xin: Agree
M: 
    slow fast pointers
    hashtable (value : next)
    singly linkedlist
    
P:
        
        s/f
        3 -> 2 -> 0 -> 4 
            |          |
                ------
    # slow, fast pointers
    inilize the slow and fast pointers to be the head of the linkedlist
    
    while loop to check if the fast and fast.next is not None 
        move slow pointer one by one slow = slow.next
        move fast pointer two by two fast = fast.next.next
        
        check if the slow is the same as the fast pointer:
            if yes, return True
    return False
I:
R:
E: Time complexity -> O(n) because one while loop
   Space complexity -> O(1) because we are not going to use any extra space or memory in our DS
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next= next
        
def solution(head):
    slowNode = head
    fastNode = head
    while fastNode and fastNode.next is not None:
        slowNode = slowNode.next
        fastNode = fastNode.next.next
        if fastNode == slowNode:
            return True
    return False
if __name__ == "__main__":
    pass
