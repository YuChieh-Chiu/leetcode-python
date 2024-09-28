class MagicDictionary:

    def __init__(self):
        self.trie = {}
    def insert_derivatives(self, word: str) -> None:
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
    def buildDict(self, dictionary: List[str]) -> None:
        """
        thought:
        - our goal is to build a dictionary that allows us to check whether a word exists in the dictionary by traversing it character by character.
        - to efficiently traverse the word one character at a time, we can use a `Trie` data structure as the dictionary.
        """        
        for word in dictionary:
            self.insert_derivatives(word)
    def dfs(self, current_node: dict, i: int, searchWord: str, modified: int):
        """
        [depth-first search (DFS)]
        thought:
        - recursively traverse each word in the `Trie`.
        - first, outside of this function, we have initialized some variables:
            - `current_node = self.trie`: indicates that we start from the root.
            - `i = 0`: indicates that we should start comparing from the first character of `searchWord`.
            - `modified = 0`: records the number of modifications made during each word traversal.
            - `self.tot = 0`: records the total number of words that fulfill the following conditions:
                (1) the length of the word equals the length of `searchWord`.
                (2) `modified = 1` (only modified once).
        - the steps are as follows for each `current_node`:
            1. if we reach the end of the word, check if the conditions above are fulfilled:
                - if fulfilled, increment `self.tot` by 1 to indicate that there is one word in the Trie that meets the condition.
                - otherwise, do nothing.
            2. to avoid an IndexError, if `i` is out of the index range of `searchWord`, assign `<eos>` to `char`; otherwise, assign the character at index `i` of `searchWord` to `char`.
            3. if the key of the `current_node` equals `char`, meaning that we don't need to modify the character, pass `modified` as a parameter to the `dfs` function. Otherwise, pass `modified + 1` to represent that a modification has been made during the traversal.
        """
        for k, v in current_node.items():
            if (k == "_end"):
                if (modified == 1) & (i == len(searchWord)):
                    self.tot += 1
            if i >= len(searchWord):
                char = "<eos>"
            else:
                char = searchWord[i]
            if k != char:
                self.dfs(v, i+1, searchWord, modified+1)
            else:
                self.dfs(v, i+1, searchWord, modified)
    def search(self, searchWord: str) -> bool:
        """
        thought:
        - our goal is to determine whether there is any word in the `Trie` that can be transformed into `searchWord` by changing only one character.
        - to achieve this, we need to traverse the word from the first to the last character, and only proceed along paths that match words in the dictionary.
        - this is effectively handled by the `depth-first search (DFS)` algorithm, so we can use this approach.
        steps:
        - initialize some variables
        - use `dfs` function
        - after executing the `dfs` function, the variable `self.tot` has been updated.
            - if `self.tot > 0`, it means that there is at least one word in the Trie that fulfills the condition described in the problem; otherwise, no such word exists.
        """
        current_node = self.trie
        i = 0
        modified = 0
        self.tot = 0
        self.dfs(current_node, i, searchWord, modified)
        if self.tot > 0:
            return True
        else:
            return False
        
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
