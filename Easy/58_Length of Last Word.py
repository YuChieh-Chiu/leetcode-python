import re
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        thought:
        - from the problem description, we understand the following:
            - the string `s` consists only of words and spaces.
            - a word is defined as a maximal substring containing only non-space characters.
        - our goal is to find the length of the LAST word in the string. To achieve this, we need to split the string by spaces and identify the LAST maximal substring that consists of non-space characters.
        - therefore, we can follow these steps:
            (1) replace multiple consecutive spaces with a single space to simplify the following operations.
            (2) split the string `s` by spaces (' ').
            (3) check if the LAST element (word) in the split list is empty:
                - if it's not empty: The LAST word can be located directly using `[-1]`.
                - if it is empty: The LAST word should be located using `[-2]`.
            (4) return the `len()` of the identified word.
        """
        s = re.sub('\s+', ' ', s)
        s_list = s.split(' ')
        if s_list[-1] == '':
            return len(s_list[-2])
        else:
            return len(s_list[-1])
