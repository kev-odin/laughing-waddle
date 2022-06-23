"""
UMPIRE  
Understand what the interviewer is asking for by using test cases and questions about the problem.  
Match what this problem looks like to known categories of problems, e.g. Linked List or Dynamic Programming and strategies or patterns in those categories.  
Plan the solution with appropriate visualizations and pseudocode.  
Implement the code to solve the algorithm.  
Review the code by running specific example(s) and recording values (watchlist) of your code's variables along the way.  
Evaluate the performance of your algorithm and state any strong/weak or future potential work.

U: 
    bao:
    far:
    jes:
    kev:
    tin:
    xin:
M:
P: 
I:
R:
E: 
"""

#
# Given a node, return the length of the linked list
#
# Input: 1 ; Return: 1
# Input: 1->2->3 ; Return 3
#
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getLength(node):
    length = 0
    while node != None:
        length += 1
        node.next = node.next.next

    return length


class Tests:
    if __name__ == "__main__":
        n0 = ListNode(0)
        print(f"Test 1 - getLength returned: {getLength(n0)}, expected: 1")

        n1 = ListNode(val=1)
        n2 = ListNode(val=2)
        n3 = ListNode(val=3)
        n1.next = n2
        n2.next = n3
        print(f"Test 2 - getLength returned: {getLength(n1)}, expected: 3")