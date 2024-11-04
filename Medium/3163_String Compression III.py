class Solution:
    def extractMaxPrefix(self, word: str) -> (str, str):
        if word == "":
            return "", word
        prefix = ""
        while (len(prefix) < 9) and (word != ""):
            if prefix == "":
                pass
            else:
                if prefix[-1] == word[0]:
                    pass
                else:
                    break
            prefix += word[0]
            if len(word) == 1:
                word = ""
                break
            else:
                word = word[1:]
        return prefix, word
    def compressedString(self, word: str) -> str:
        """
        thought:
        - Objective: Given a string `word`, use the following custom algorithm to compress it:
            (1) Create an empty string `comp`.
            (2) Iteratively remove the longest prefix from `word` and add the `{num}{char}` combination of the prefix’s length and character to `comp`, repeating until `word` is empty.
                - Definition of prefix: A prefix is a substring consisting of a single repeated character, with a maximum length of 9.
        - Steps:
            (1) Create an empty string `comp`.
            (2) Define the function `extractMaxPrefix`, which performs the following tasks:
                - Check if the string `word` is empty; if so, return '' and `word`.
                - Create an empty string `prefix` to store the longest prefix to be removed from `word`.
                - While the length of `prefix` is less than 9, the next character matches the previous, and `word` is not empty, continue traversing `word`, removing characters one by one from the front. Stop when any condition is not met, and return `prefix` and the updated `word`.
            (3) Using the results from the previous step, if `prefix` is not empty, continue adding the `{num}{char}` combination of the prefix's length and character to `comp`; otherwise, exit the while loop and return the result.
        """

        comp = ""
        while True:
            prefix, word = self.extractMaxPrefix(word)
            if prefix == "":
                break
            else:
                comp += f"{len(prefix)}{prefix[0]}"
        return comp
