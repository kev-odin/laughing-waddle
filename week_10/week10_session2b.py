"""
Problem #2: Binary Tree Paths

Given a binary tree, print/return all root-to-leaf paths.

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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val}"


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
