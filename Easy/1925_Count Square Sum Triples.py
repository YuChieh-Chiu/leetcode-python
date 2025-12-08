import math
class Solution:
    def countTriples(self, n: int) -> int:
        """
        Thought:
        - Goal: Count the number of square triples (a, b, c) such that a^2 + b^2 = c^2 and 1 <= a, b, c <= n.
        - Idea: Use a nested loop to iterate through all possible pairs of (a, b) where 1 <= a, b <= n. Calculate c and check if it is a valid integer triple.
        - Steps:
            1. Initialize a counter `total` to 0.
            2. Iterate `a` from 1 to `n` (inclusive).
            3. Inside, iterate `b` from 1 to `n` (inclusive).
            4. Calculate $c = \sqrt{a^2 + b^2}$.
            5. **Optimization:** If $c > n$, since $c$ will only increase as $b$ increases, break the inner loop (for $b$).
            6. If $c$ is an integer, increment `total`.
            7. Return `total`.
        - Time Complexity: O(n^2)
        - Space Complexity: O(1)
        """
        total = 0

        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c = math.sqrt(a**2 + b**2)
                if c > n:
                    break
                if c.is_integer():
                    total += 1

        return total
