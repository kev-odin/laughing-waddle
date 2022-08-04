"""
Problem #2: Binary Tree Paths

Given a binary tree, print/return all root-to-leaf paths.

U:
    bao: What order should the nodes be printed? Order of visited.
    far: Can we be given an empty tree? No, you will be given at least one node.
    jes: What should our question output? List of list traveral value.
    kev: Driver.
    tin: Would bfs be helpful in this situation?
    xin: What if there are no children? Just print the root.
M:
    DFS to find the paths
    Using a set for seen nodes
P:
    global currentPath = []
    global totalPath = []
    dfs(root):
        if not root.left and not root.right:
            totalPath.append(currentPath[:])
        currentPath.append(root.val)
        dfs(root.left)
        dfs(root.right)
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
            [[1, 2, 4], [1, 3, 5]]
    Another Tree:
                1
               / \
              2   3
             / \
            4   5
            [[1, 3], [1, 2, 4], [1, 2, 5]]
    Best Tree:
                1
               / \
              2   3
             / \   \
            4   5   6
            [[1, 2, 4], [1, 2, 5], [1, 3, 6]]

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
