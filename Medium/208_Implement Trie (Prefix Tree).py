class Trie:

    def __init__(self):
        """
        concept:
        - initialize a dictionary as a Trie data structure
        """
        self.trie = {}
    def insert(self, word: str) -> None:
        """
        concept:
        - traverse the word character by character:
            - if the current character reaches the end of a branch in the Trie, return the Trie.
            - otherwise, continue traversing the word:
                - if the character already exists in the current branch, proceed to the next character.
                - if the character does not exist, insert an empty dictionary as a new branch.
                - after processing the character, move to the next branch.
        - after the word has been fully traversed but hasn't reached the end of a branch in the Trie, append an empty dictionary to mark the word's presence in the Trie.
        """
        current_node = self.trie
        for char in word:
            if current_node == {"_end"}:
                return self.trie
            else:
                if char in current_node:
                    pass
                else:
                    current_node[char] = {}
                current_node = current_node[char]
        current_node["_end"] = {}
    def search(self, word: str) -> bool:
        """
        goal:
        - the word must fully match in the Trie, reaching the end of a valid branch.
        concept:
        - traverse the word character by character:
            - if the character is found in the current branch, proceed to the next.
            - if the character is missing, return `False`, indicating the word is not in the Trie.
        - after traversing the word, if we have reached the end of a valid branch, return `True` to confirm the word's existence in the Trie.
        - otherwise, return `False`.
        """
        current_node = self.trie
        for char in word:
            if char in current_node:
                current_node = current_node[char]
            else:
                return False
        if "_end" in current_node:
            return True
        return False            
    def startsWith(self, prefix: str) -> bool:
        """
        goal:
        - only need to ensure the prefix fully matches in the Trie.
        concept:
        - traverse the prefix character by character:
            - if the character exists in the current branch, continue to the next.
            - if the character is missing, return `False`, indicating the prefix does not exist.            
        - after traversing the prefix, return `True` if the prefix exists in the Trie.
        """
        current_node = self.trie
        for char in prefix:
            if char in current_node:
                current_node = current_node[char]
            else:
                return False            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
