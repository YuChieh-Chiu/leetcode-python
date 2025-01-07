class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """
        Thought:
        - Goal:
            - Given an array of strings `words`, return all strings in `words` that are substrings of another word.
        - Problem Description:
            - Substring: A contiguous sequence of characters within a string. This implies the length of the substring must be less than or equal to the length of the original string.
        - Steps:
            1. Sort the list `words` by the length of its elements, ensuring longer words are checked first.
            2. Initialize a set to store all unique substrings found.
            3. Use nested loops to iterate through the list `words` and check for substrings:
                - For each word in the list `words`, compare it only with subsequent words in the list.
                - If the subsequent word is a substring of the current word, add it to the set using `.add()`.
            4. Convert the set into a list and return it.
        """

        # sort by length descendingly
        words = sorted(words, key=lambda x:len(x), reverse=True)
        
        # check for substring
        substrings = set()
        for i, word1 in enumerate(words):
            for word2 in words[i+1:]:
                if word2 in word1:
                    substrings.add(word2)

        return list(substrings)
