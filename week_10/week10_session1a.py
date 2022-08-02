"""
Problem #1: Identical Trees

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Examples:
https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg

Input: p = [1,2,3], q = [1,2,3] 
Output: true

https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg
Input: p = [1,2], q = [1,null,2]
Output: false

https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg
Input: p = [1,2,1], q = [1,1,2]
Output: false

U:
    bao:What if both trees are null? would it be true or false?
    far:Do we know if it is BST or not? No we don't
    jes:What is the maximum depth of the tree? (0-100)
    kev:Do we have any memory restriction with the solution?recursive? iteretive?
    Can we assume the tree is complete?
    tin:how height of trees can we expect? one node at least(height is at least one)
    xin:Agree 
M:
Preorder traversal
Recurssion

P:
-base case: check if the nodes are the same 
-check if leaf nodes of the trees are the same
  if not return false
  else return true
  

I:
R:
E:
"""
def sameTree(node1, node2):
    if (node1 and node2) is None:
        return True
        
    if not node1 or not node2:
        return False
        
    if node1.val != node2.val:
        return False
        
    return sameTree(node1.right, node2.right) and sameTree(node1.left, node2.left)
    
if __name__ == "__main__":
    pass
