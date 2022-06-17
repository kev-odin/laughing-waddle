"""
Problem #1: Remove Duplicates from Sorted List
Given a sorted linked list, delete all duplicates such that each element appear only once.

Examples:

Input: 1->1->2  
Output: 1->2  

Input: 1->1->2->3->3  
Output: 1->2->3

UMPIRE  
Understand what the interviewer is asking for by using test cases and questions about the problem.  
Match what this problem looks like to known categories of problems, e.g. Linked List or Dynamic Programming and strategies or patterns in those categories.  
Plan the solution with appropriate visualizations and pseudocode.  
Implement the code to solve the algorithm.  
Review the code by running specific example(s) and recording values (watchlist) of your code's variables along the way.  
Evaluate the performance of your algorithm and state any strong/weak or future potential work.  

U:
    bao:In what order is the list sorted, increasing or decreasing?
    -What if there is a cycle in the list?
    far: Are we always going to have a duplicate element?
    jes:acending decending?!
    kev:What happens if we get an empty list?
    tin:
    xin:What if the list is all duplicate elements? or all 1s, 2s?
M:
    -Linked list
    -Two pointers
    -dummy node to eliminate the edge case

P:
    -create a current pointer to point to the head
    -Create a pointer to point to the head node 
    -while loop to iterate the linked list 
    -if the next node is equal to the current node make the next pointer point to the
    next next node 
    else:
    -current node equals current node points to next node
    -return the head of the linked list 
 
I: See below.
R: See below.
E:
    Time: O(n) because of the while loop, and single traversal
    Space: O(1) because no extra DS or memory used for solution
"""


class Node:
    def __init__(self, next=None, val=None):
        self.next = next
        self.val = val

    def __str__(self):
        return str(self.val)


def solution(head):
    current = head

    if not head:
        return False

    while current:
        if current.next is None:
            return head  # reached the end
        elif current.val == current.next.val:
            current.next = current.next.next  # duplicate node
        else:
            current = current.next

    return head


if __name__ == "__main__":
    test = Node(Node(Node(val=1), val=2), val=2)
    print(solution(test))
