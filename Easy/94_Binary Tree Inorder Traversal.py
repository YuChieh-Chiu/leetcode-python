# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self) -> None:
        self.output = []

    def recursion(self, current: Optional[TreeNode]):      

        if current is None:
            return

        self.recursion(current.left)
        self.output.append(current.val)
        self.recursion(current.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Thought:
        - Goal
            - Return the inorder traversal of the tree's node values.
        - Order of Inorder Traversal
            - Left -> Root -> Right
        - Steps:
            1. If the root is `None`, return an empty list directly.
            2. Initialize a global variable, `self.output`, to store the result of the inorder traversal.
            3. Define a recursive function to perform the inorder traversal:
                - Base case: If the current node is `None`, it indicates the end of the recursion.
                - Recursive steps: 
                    - Traverse the left subtree recursively.
                    - Process the value of the current (root) node.
                    - Traverse the right subtree recursively.
            4. Call the recursive function, update `self.output`, and return the result.
        """

        if root is None:
            return []

        self.recursion(root)

        return self.output
