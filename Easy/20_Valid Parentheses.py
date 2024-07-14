class Solution:
    def isValid(self, s: str) -> bool:
        """
        thought:
        - this problem is one of the most basic examples of using the `stack` data structure.
        - we know that a valid string must satisfy the following conditions:
            (1) open brackets must be closed by the same type of brackets.
            (2) open brackets must be closed in the correct order.
            (3) every close bracket has a corresponding open bracket of the same type.
        - in other words, the rightmost open bracket must match the leftmost close bracket.
        - therefore, we can follow these steps:
            (1) establish a mapping between open brackets and close brackets.
            (2) traverse from left to right, pushing open brackets onto the `stack`, and checking close brackets against the last open bracket in the stack:
                - if they match: pop the last open bracket from the stack and continue.
                - if they do not match: return False.
        """
        brackets = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = ["<BOS>"] # add a string in list to prevent `stack[-1]` from encountering error
        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            else:
                if brackets[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack == ["<BOS>"]:
            return True
        else:
            return False
