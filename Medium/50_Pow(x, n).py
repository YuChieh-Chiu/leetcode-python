class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Thought:
        - Problem Constraints:
            - Either `x` is not zero, or `n` is greater than 0.
        - Goal:
            - Calculate `x` raised to the power of `n` and return the result as a float.
        - Key Concept:
            - If `n` equals 0, return 1 directly.
            - Otherwise, use a Binary Exponentiation approach.
                - If `n` is less than 0, compute `pow(x, n)` as `pow(1/x, -n)`.
                - we don't use recursion because the range of n is large, which can lead to `RecursionError: maximum recursion depth exceeded in comparison`
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        # Binary Exponentiation
        ans = 1
        while n > 0:
            if n % 2 == 1:  # if `n` is odd
                ans *= x
            x *= x
            n //= 2
        return ans
