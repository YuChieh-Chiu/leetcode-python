# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, current, path, root_to_leaf):
        if current.left is None and current.right is None:
            root_to_leaf.append("->".join(map(str, path)))
            # IMPORTANT：we should not append `path` variable directly to the list `root_to_leaf` when we are testing, because `path` would be modified during the recursion and it would result in a wrong answer being added into the list.
            return
        if current.left is not None:
            path.append(current.left.val)
            self.dfs(current.left, path, root_to_leaf) # recursion
            path.pop() # backtracking : "undoing" a choice
        if current.right is not None:
            path.append(current.right.val)
            self.dfs(current.right, path, root_to_leaf) # recursion
            path.pop() # backtracking : "undoing" a choice
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        thought:
        - The goal is to find and record every possible path from the root node to each leaf node in a binary tree.
        - In a binary tree, each node has up to two children: a left and a right node.
        - A path should stop once it reaches a leaf node (a node with no children).
        - Solution:
            - We can use Depth-First Search (DFS) with backtracking to explore each possible path.
            - For each node, check both the left and right children, recursively traversing down each path until we reach a leaf node.
            - Backtracking allows us to explore all possible routes from the root to each leaf by "undoing" a choice and returning to explore other options.
        - Steps:
            (1) Start from the root node, initializing the path with the root node's value.
            (2) Recursively check both the left and right children.
If the current node is a leaf node (both children are None), record the path.
            (3) If the current node has a left child, add it to the path, recursively search down the left subtree, then backtrack.
            (4) Similarly, if there is a right child, add it to the path, recursively search down the right subtree, then backtrack.
            (5) Repeat this process until all paths from the root to each leaf are recorded.
        """
        root_to_leaf = []
        self.dfs(root, [root.val], root_to_leaf)
        return root_to_leaf
