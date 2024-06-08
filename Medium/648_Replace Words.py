class Solution:
    """
    thought:
    - first, intuitively, we might want to store the strings in `list` format and then compare each string one by one to see if it contains the root, but this approach would have a time complexity of `O(mn)`, which is too time-consuming.
    - so, we might want to use data structure like `trie` to solve this question.
    reference:
    - the idea of the following code came from the reference below
        ``` reference
        - author : 辛西亞．Cynthia
        - article url link : https://hackmd.io/@CynthiaChuang/LeetCode-0208-Implement-Trie
        ```
    """
    def __init__(self) -> None:
        self.trie = {}
    def insert_derivative(self, word: str) -> None:
        current_node = self.trie
        for char in word:
            last_node = current_node
            if current_node == {"_end"}: # because we only need the shortest derivative, if we already get it, we can just return `trie`
                return self.trie
            else:
                if char in current_node:
                    pass
                else:
                    current_node[char] = {}
                current_node = current_node[char]
        last_node[char] = {"_end"} # just for clear print result
    def find_sentence(self, word: str) -> bool:
        current_node = self.trie
        derivative_exist = True
        derivative = ""
        for char in word:
            derivative += char
            if char in current_node:
                current_node = current_node[char]
                if current_node == {"_end"}:
                    break
                else:
                    pass
            else:
                derivative_exist = False
                break
        return derivative_exist, derivative
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # build trie
        for derivative in dictionary:
            self.insert_derivative(word=derivative)
        # search trie
        derivative_sentence = []
        for word in sentence.split(" "):
            derivative_exist, derivative = self.find_sentence(word=word)
            if derivative_exist:
                derivative_sentence.append(derivative)
            else:
                derivative_sentence.append(word)
        derivative_sentence = " ".join(derivative_sentence)
        return derivative_sentence
