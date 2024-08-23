class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        thought:
        - the goal is to determine if the substring `needle` exists within the string `haystack`, and if so, return the index of its first occurrence.
        - there are two approaches:
        1. the easiest method is to use the Python built-in function `str.find()`.
        2. alternatively:
            (1) check if the length of `haystack` is greater than `needle`.
                - If it is, proceed to step (2).
                - If not, return -1.
            (2) loop through each substring in `haystack` with the same length as `needle`:
                - If a substring matches `needle`, return the index of its first occurrence.
                - If not, continue.
            (3) if no matching substring is found after the loop, return -1.
        """

        # 1. str.find()
        # return haystack.find(needle)

        # 2. slice substring from haystack to compare with needle
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
