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
# Given a sorted linked list, delete all duplicates such that each element appear only once.
# Input : 1 ; Output : 1
# Input : 1->1 ; Output: 1
# Input : 1->1->1->2->2 ; Output: 1->2
#
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def equals(self, n):
        if self.val != n.val:
            return False

        if self.next == None:
            if n.next != None:
                return False
            else:
                return True

        return ListNode.equals(self.next, n.next)


def removeDuplicates(head):
    if head == None or head.next == None:
        return head
    curNode = head

    if curNode.val == curNode.next.val:
        curNode.next = curNode.next.next
    else:
        curNode = curNode.next

    return head


class Tests:
    if __name__ == "__main__":
        n1_1 = ListNode(1)
        print("Test cases 1 passed: " + str(removeDuplicates(n1_1).equals(n1_1)))

        n2_1a = ListNode(1)
        n2_1b = ListNode(1)
        n2_1a.next = n2_1b

        n2_answer = ListNode(1)
        print("Test case 2 passed: " + str(removeDuplicates(n2_1a).equals(n2_answer)))

        n3_1a = ListNode(1)
        n3_1b = ListNode(1)
        n3_2a = ListNode(2)
        n3_2b = ListNode(2)
        n3_1a.next = n3_1b
        n3_1b.next = n3_2a
        n3_2a.next = n3_2b

        n3_answer1 = ListNode(1)
        n3_answer2 = ListNode(2)
        n3_answer1.next = n3_answer2

        print("Test case 3 passed: " + str(removeDuplicates(n3_1a).equals(n3_answer1)))
