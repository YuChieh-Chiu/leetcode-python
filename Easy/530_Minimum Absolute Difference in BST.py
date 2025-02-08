# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.minimum = 100000
        self.prev = None

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        Thought:
        - Two key points:
            1. The characteristic of a BST is that an in-order traversal (left -> root -> right) results in node values in ascending order.
            2. Only the previous node value (`prev`) needs to be recorded for comparison.

        Steps:
        1. Define `self.minimum` to track the smallest difference and `self.prev` to record the previous node value during the in-order traversal.
        2. Define the in-order traversal function with the following operations:
            - Termination condition: If the current node is `None`, the recursion stops.
            - Recursive order: First traverse the left subtree, then process the current node, and finally traverse the right subtree.
            - Processing the current node: Compare the absolute difference between self.prev and the curret node value with `self.minimum` to update the smallest difference, and update `self.prev`.
        3. Call the in-order traversal function and return `self.minimum`.
        """

        def inorder_traversal(current: Optional[TreeNode]):

            if current is None:
                return

            inorder_traversal(current.left)
            if self.prev is not None:
                self.minimum = min(self.minimum, current.val - self.prev)
            self.prev = current.val
            inorder_traversal(current.right)

        inorder_traversal(root)

        return self.minimum
