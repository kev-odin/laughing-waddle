"""
Problem #1: Insert into a BST

Given the root node of a binary search tree (BST) and a value to be inserted
into the tree, insert the value into the BST.

Example:

Input: root = [4, 2, 7, 1, 3], val = 5
           4     
          / \
         2   7
        / \   
       1   3   

Output: [4, 2, 7, 1, 3, 5]    
            4     
          /    \
         2      7
        / \    / 
       1   3  5
       
Another accepted tree is: [5, 2, 7, 1, 3, null, null, null, 4]
            5     
          /   \
         2     7
        / \     
       1   3
            \
             4  

U:
    Bao: Is the tree balanced?
    Kevin: Are values in the tree unique?
    Jessica: Is the tree completed?
    Farnoosh: Please feel free to add more questions
    Xingguo: Please feel free to add more questions
    Tin: What if the root is empty? Then, ignore null. Create a new node and return the value.
M:
- Recursion
- DFS (Bao: PostOrder) (Kevin: PreOrder)
P:
    Check the root is None or not:
        - If root is None:
            return new node(value)
    Check value if it is less or greater than root node:
        - If the value greater than root:
            - Go right and insert the value
        - Else:
            - Go left and insert the value
    return root
I: Shown below
R:
E: 
    Time: O(log N) if balanced, unbalanced O(N)
    Space: O(log N) if balancedl, unbalanced O(N)
             
"""

def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None:
        return TreeNode(val)
    if val > root.val:
        root.right = self.insertIntoBST(root.right, val)
    else:
        root.left = self.insertIntoBST(root.left, val)
    return root
