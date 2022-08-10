"""
Problem #2: Validate BST

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Examples:

Input: root = [2, 1, 3]
           2     
          / \
         1   3 

Output: true
       
Input: root = [5,1,4,null,null,3,6]
           5     
          / \
         1   4
            / \
           3   6 

Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


U:
    bao: what if it's not balanced?
    far: will we see unique nodes? any duplicates allowed?
    jes: driver
    kev: is it a complete tree?
    tin: what if a root is empty or null?
    xin: missing :(
M:

P:
bounds(node, left, right):
    r

validate(root, )
    if not node:
        True
    if node.val < right and node.val  > left:
        return False
    return bounds(node.left, leftbound, node.val)

I:
R:
E:

"""


if __name__ == "__main__":
    pass
