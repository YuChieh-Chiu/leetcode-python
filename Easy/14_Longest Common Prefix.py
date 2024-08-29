class Solution:
    def __init__(self) -> None:
        self.trie = {}
    def insert_derivative(self, word: str) -> None:
        current_node = self.trie
        for char in word:
            last_node = current_node
            if current_node == {"_end"}:
                return self.trie
            else:
                if char in current_node:
                    pass
                else:
                    current_node[char] = {}
            current_node = current_node[char]
        last_node[char] = {"_end"}
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        thought:
        1. our goal is to find the longest common prefix among an array of strings.
        2. to achieve this, we can use a `Trie` data structure to efficiently store and search prefixes.
        3. steps to follow:
           (1) build a `Trie` to store all strings:
               - If any string in `strs` is "", the longest common prefix is "", so we return "" immediately.
               - Since we only need the common prefix, we store only the shortest derivatives in the `Trie`.
           (2) define a variable `longestPrefix` to store the longest common prefix found.
           (3) traverse the `Trie` to determine the longest common prefix:
               - If the current level in the `Trie` has only one child node and that child node marks the end of a word (`'_end'`), we return the prefix found so far.
               - If the current level has only one child node but it does not mark the end of a word, continue traversing to extend the `longestPrefix`.
               - If the current level has more than one child node, we have reached the end of the longest common prefix and can return it.

        """
        # build trie
        for word in strs:
            if word == "":
                return ""
            self.insert_derivative(word=word)
        # record the longest common prefix
        longestPrefix = ""
        # search the longest common prefix
        current_lvl = self.trie
        while True:
            if len(current_lvl.keys()) == 1:
                node = list(current_lvl.keys())[0]
                longestPrefix += node
                if current_lvl[node] == {"_end"}:
                    return longestPrefix
                else:
                    current_lvl = current_lvl[node]
            else:
                return longestPrefix
