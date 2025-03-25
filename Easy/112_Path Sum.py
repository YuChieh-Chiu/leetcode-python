# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Thought:
        - Goal:
            - Given the root of a binary tree and an integer `targetSum`, return `True` if the tree has a root-to-leaf path such that the sum of all values along the path equals `targetSum`.
        - Idea:
            - Use a recursive traversal from root to leaf.
        - Steps:
            1. If `root` is `None`, return `False` immediately.
            2. Define a recursive function that traverses the binary tree:
                - Base Case: When the current node is a leaf (i.e., both left and right are `None`), return whether `currentSum + node.val` equals `targetSum`.
                - Recursive Step:
                    - Increment `currentSum` by the value of the current node.
                    - Recursively call the function on the left and right children.
                    - Return the logical OR of the results from the left and right subtrees.
            3. Execute the recursive function starting from the root with an initial `currentSum` of 0 and return the result.
        """

        if root is None:
            return False

        def dfs(node: Optional[TreeNode], currentSum: int) -> bool:
            if node is None:
                return False
            
            currentSum += node.val
            # 若為葉節點，則檢查目前累加的和是否等於 targetSum
            if node.left is None and node.right is None:
                return currentSum == targetSum
            
            return dfs(node.left, currentSum) or dfs(node.right, currentSum)
        
        return dfs(root, 0)
