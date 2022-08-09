"""
Problem #1: Print Binary Tree

Given a binary tree, print all its leaf nodes from left to right

Extra Challenge: 
If we are asked to print the leaf nodes from right to left, how would you change your solution?

U:
    bao: What if the tree only have right leaf nodes? Print the only leaf node
    far: Agree with others
    jes: There are leaf nodes at different levels? Yes
    kev: Can the input tree be null? Assume that the tree is not null
    tin: What are height and depth of the tree? 1-infinity
    xin: Can we use extra space? Any space constraints?  Yes, no constraint
M:
Depth-first Search
Recursion
🍞 first search
P:
Base case:
Check if the root is not null

Traverse down the tree from the left and then the right.
Check if the node have any children (if the node is a leaf node or not), if not then print the node.
I:
R:
E:
    Time: O(N) or O(h)
    Space: O(1)

1
 \
  1
   \
    1
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val}"


def solution(root):
    if not root:
        return

    if not root.left and not root.right:
        print(root.val)

    solution(root.left)
    solution(root.right)


if __name__ == "__main__":
    """
    Basic Tree:
                1
               / \
              2   3
             /     \
            4       5
    Another Tree:
                1
               / \
              2   3
             / \
            4   5
    Best Tree:
                1
               / \
              2   3
             / \   \
            4   5   6

    """
    basic = TreeNode(
        1, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(3, right=TreeNode(5))
    )

    another = TreeNode(
        1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3)
    )

    best = TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
        right=TreeNode(3, right=TreeNode(6)),
    )

    solution(basic)
    solution(another)
    solution(best)
