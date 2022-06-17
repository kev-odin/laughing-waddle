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
- the plan
initialize two pointers:
initialize a dummy node pointing to nothing
while loop both are not none?
compare the two values of the two pointers, 
    value that is less added to the dummy node
    increment the pointer

I: see below
R: see below. need to implement a linked list
E: 
    * Time: O(n) because of the traversal of both lists
    * Space: O(1) because no additional data structure is used to store information
"""


class Node:
    def __init__(self, dataval=None):
        self.val = dataval
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None


def solution(leftLst, rightLst):
    leftNode = leftLst
    rightNode = rightLst
    #       need to make two pointers dummy node needs to stay at the
    #       head while current makes connections; we swtiched it
    dummyNode = curr = Node()

    while leftNode and rightNode:
        if leftNode.val < rightNode.val:
            dummyNode.next = leftNode
            leftNode = leftNode.next
            print(dummyNode.val)
        else:
            dummyNode.next = rightNode
            rightNode = rightNode.next
            print(dummyNode.val)
        dummyNode = dummyNode.next

    # the rest of the values are already linked so we just need to connect the
    # last node to connect to the rest of the other list
    if leftNode or rightNode:
        dummyNode.next = leftNode if leftNode else rightNode
        print(dummyNode)
    return curr.next


if __name__ == "__main__":
    pass
