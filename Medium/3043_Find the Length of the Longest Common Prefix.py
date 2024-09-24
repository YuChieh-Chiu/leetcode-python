class Solution:
    def __init__(self) -> None:
        self.trie = {}
        self.max_length = 0
    def insert_derivative(self, word: str) -> None:
        current_node = self.trie
        for char in word:
            if char in current_node:
                pass
            else:
                current_node[char] = {}
            current_node = current_node[char]
    def search_trie(self, word: str) -> int:
        length = 0
        current_node = self.trie
        for char in word:
            if char in current_node:
                length += 1
            else:
                return length
            current_node = current_node[char]
        return length
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        """
        thought:
        - our goal is to find the length of the longest common prefix among all pairs from two arrays.
        - based on the problem description, we know two pieces of information:
            (1) a prefix of a positive integer is formed by one or more of its leftmost digits.
            (2) each pair (x, y) consists of x from `arr1` and y from `arr2`.
        - since our goal is to find the longest common prefix between `arr1` and `arr2`, we can use a Trie data structure to store the digits of integers from one array and search for common prefixes in the other array.
        - the following steps can be taken:
            (1) initialize a Trie data structure and a variable to track the maximum length, initially set to zero.
            (2) insert the digits of each integer from `arr1` into the Trie.
            (3) traverse each integer in `arr2` and search the Trie to calculate the length of the longest common prefix for each integer.
            (4) determine the maximum length among all the longest common prefix lengths.
        """
        # build Trie
        for word in arr1:
            self.insert_derivative(str(word))

        # search Trie
        for word2 in arr2:
            length = self.search_trie(str(word2))
            if length > self.max_length:
                self.max_length = length
        
        return self.max_length
