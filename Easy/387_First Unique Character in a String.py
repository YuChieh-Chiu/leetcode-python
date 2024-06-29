class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        thought:
        - we need to find the FIRST non-repeating character in the string `s`
        - so we have to traverse through `s` one time
        - we have to store a SET of repeating characters and a LIST of non-repeating yet character in list (use list to represent queue - FIFO)
            - if character in repeating, pass
            - if not
                - if character in non-repeating, means that that's the first time the character repeats, we should remove it from non-repeating list and add it into repeating set
                - if not, append new non-repeating character at the end of list (FI)
            - finally, get the index of the fist element (FO)
        """
        repeating = set()
        non_repeating = []
        for c in s:
            if c in repeating:
                pass
            else:
                if c in non_repeating:
                    non_repeating.remove(c)
                    repeating.add(c)
                else:
                    non_repeating.append(c)
        if len(non_repeating) == 0:
            return -1
        else:
            return s.find(non_repeating[0])
