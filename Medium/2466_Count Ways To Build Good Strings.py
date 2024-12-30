class Solution:
    def __init__(self) -> None:
        self.memo = {} # {remaining_cnt: numbers}

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """
        Thought:
        - Goal:
            - Given the integers `zero`, `one`, `low`, and `high`, calculate the number of different good strings.
                - The result should be returned modulo (10**9+7).
        - Definition of Good Strings:
            - A good string is constructed by the following process, with its length falling between low and high (inclusive):
                - At each step, either append the character '0' zero times or append the character '1' one times.
        - Idea:
            - Since good strings with different lengths are inherently distinct, we can focus on calculating the number of good strings for each specific length.
            - As each step depends on the results of the previous steps, we should use a dynamic programming algorithm with memoization.
        - Steps:
            1. Initialization:
                - Create a dictionary `self.memo = {}` to store the number of good strings for each remaining length.
                    - Example: {remaining_length: number_of_good_strings}.
            2. Recursive Function:
                - Base Case:
                    - If remaining_length == 0, it indicates that a good string has been found, so return 1.
                    - If remaining_length < 0, it means the string is invalid, so return 0.
                - Recursive Relation:
                    - For remaining_length > 0, recursively calculate by subtracting zero or one from the remaining length.
                        - Tips: To prevent `Memory Limit Exceeded`, we should use modulo on the result of each step.
            3. Output:
                - Iterate over the lengths from low to high. For each length, call the function with the current length and accumulate the results.
            4. Modulo:
                - Use modulo (10**9+7) on the final result to ensure correctness.
        - Topics:
            - Dynamic Programming, Memoization.
        """
        # Modulo
        MOD = 10**9 + 7

        def dfs(remaining_length: int) -> int:
            # Base case
            if remaining_length == 0:
                return 1 
            if remaining_length < 0:
                return 0

            # Memoization
            if (remaining_length) in self.memo:
                return self.memo[remaining_length]

            # Recursion relation
            substract_zero = dfs(remaining_length - zero)
            substract_one = dfs(remaining_length - one)

            self.memo[remaining_length] = (substract_zero + substract_one) % MOD

            return self.memo[remaining_length]

        total_cnt = 0
        for length in range(low, high+1):
            total_cnt += dfs(length)
            total_cnt %= MOD
        
        return total_cnt
