class Solution:
    def smallestSubsequence(self, s: str) -> str:
        """
        Thought:
        - Goal: Find the lexicographically smallest subsequence of `s` that contains all unique characters exactly once.
        - Idea: Use a monotonic stack combined with a greedy approach. We maintain a stack of characters that are sorted lexicographically as much as possible. If we see a smaller character, we can pop the larger characters from the stack, but only if those larger characters appear again later in the string.
        - Steps:
            1. Record the last occurrence index of each character in `s`.
            2. Iterate through `s` character by character.
            3. If the character is already in our stack (tracked by `seen` set), skip it.
            4. While the stack is not empty, the current character is smaller than the top of the stack, and the top character will appear again later: pop the top character from the stack and remove it from `seen`.
            5. Push the current character onto the stack and add it to `seen`.
            6. Join the stack into a string and return it.
        - Time Complexity: O(N), where N is the length of string `s`.
        - Space Complexity: O(K), where K is the number of distinct characters in `s` (K <= 26).
        """
        last_idx = {char:i for i, char in enumerate(s)}
        stack = []
        seen = set()

        for i, char in enumerate(s):
            if char not in seen:
                while (
                    stack and
                    last_idx[stack[-1]] > i and
                    char < stack[-1]
                ):
                    seen.remove(stack[-1])
                    stack.pop()
                stack.append(char)
                seen.add(char)

        return "".join(stack)
