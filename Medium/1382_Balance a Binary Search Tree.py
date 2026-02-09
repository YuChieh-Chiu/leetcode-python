# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Thought:
        - Goal: Reconstruct a given Binary Search Tree (BST) into a height-balanced BST.
        - Idea: A balanced BST can be efficiently built from a sorted sequence by picking the median as the root.
        - Steps:
            1. Perform an in-order traversal to extract all node values into a sorted list.
            2. Use a divide-and-conquer approach to recursively pick the middle element of the sorted list as the current node's root.
            3. Construct the left and right subtrees from the remaining halves of the list.
        - Time Complexity: O(n) - We visit each node once during traversal and once during reconstruction.
        - Space Complexity: O(n) - We store all node values in a list of size n, plus the recursion stack.
        """        
        vals = []
        
        # 負責蒐集數值的閉包函式
        def _in_order(node):
            if node:
                _in_order(node.left)
                vals.append(node.val)
                _in_order(node.right)

        # 負責重建樹的閉包函式
        def _build_tree(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            curr = TreeNode(vals[mid])
            curr.left = _build_tree(left, mid - 1)
            curr.right = _build_tree(mid + 1, right)
            return curr

        _in_order(root)
        return _build_tree(0, len(vals) - 1)
