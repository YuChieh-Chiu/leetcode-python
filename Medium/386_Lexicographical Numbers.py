class Solution:
    def __init__(self) -> None:
        self.trie = {}
        self.node = ""
        self.lexicalOrderList = []
    def insert_derivative(self, word: str) -> None:
        current_node = self.trie
        for char in word:
            if char in current_node:
                pass
            else:
                current_node[char] = {}
            current_node = current_node[char]
    def depth_first_search(self, current_node: dict) -> None:
        for k, v in current_node.items():
            self.node += str(k)
            self.lexicalOrderList.append(int(self.node))
            if v == {}:
                self.node = self.node[:-1] # backtrack
            else:
                current_node = v # go to the next level
                self.depth_first_search(current_node) # traverse through all nodes at the next level
        self.node = self.node[:-1] # after traversing the current level, backtrack to its parent level
    def lexicalOrder(self, n: int) -> List[int]:
        """
        thought:
        - our goal is to sort integers from 1 to n in lexicographical order.
        - lexicographical order means sorting numbers digit by digit, such as: 1, 10, 11, ..., 100, ..., 2, ...
        - we can use a Trie data structure to store the integers digit by digit and apply a Depth-First Search (DFS) algorithm to ensure the result is in lexicographical order.
            - the steps for Depth-First Search (DFS) are recursive, and the core concept is as follows:
                # Core concept: Go as deep as possible before backtracking. This means we should keep digging deeper until we reach the bottom of the Trie.
                # Steps:
                    1. Use a for loop to traverse through the Trie.
                        - If we cannot go deeper (i.e., we've reached the bottom of the Trie), record the value and backtrack to the parent node.
                        - If we can go deeper, record the value and call the function recursively to explore further down the Trie.
                    2. After completing each for loop, we have traversed all nodes at the current sub-level of the Trie. We then backtrack to the parent node to start another recursive loop.
        - the steps to achieve this are:
            (1) Build a Trie to store the integers from 1 to n.
            (2) Use recursion to perform Depth-First Search (DFS): traverse the Trie deeply first, then broadly, and append the results to the answer list.
            (3) Return the answer list.
        """
        # build Trie
        for i in range(1, n+1):
            self.insert_derivative(str(i)) 
        # use recursion to perform Depth-First Search (DFS)
        current_node = self.trie
        self.depth_first_search(current_node)
        return self.lexicalOrderList
