class Solution:
    def climbStairs(self, n: int) -> int:
        """
        thought:
        - Our goal is to find the number of distinct ways to climb to the top of the stairs.
        - Based on the problem description, we have two options while climbing stairs: taking 1 step or 2 steps. This means we need to calculate all distinct combinations of these steps.
        - Let's consider examples where n ranges from 1 to 4:
            n = 1 -> 1 way: (1)
            n = 2 -> 2 ways: (1+1) or (2)
            n = 3 -> 3 ways: (1+1+1), (2+1), or (1+2)
            n = 4 -> 5 ways: (1+1+1+1), (1+1+2), (1+2+1), (2+1+1), or (2+2)
        - We can observe that:
            - f(1) = 1
            - f(2) = 2
            - For n ≥ 3, f(n) = f(n-1) + f(n-2)
        - As shown above, the structure of climbing stairs is similar to the Fibonacci sequence, which means we can use a dynamic programming algorithm to solve this problem.
        - Therefore, we can follow these steps:
            1. Initialize a list to store the values of f(k) that we have already calculated.
            2. Traverse numbers from 1 to n:
                - If the number is 1 or 2, append f(1) or f(2) to the list.
                - Otherwise, calculate f(number) by adding the values at indices (number-2) and (number-3) in the list (considering zero-based indexing), then append the result to the list.
                    - Remember that Python lists are zero-indexed, so we need to adjust the indices accordingly.
            3. Finally, retrieve the last element of the list as our answer.
        """
        memo = []
        for i in range(1,n+1):
            if i in [1,2]:
                memo.append(i)
            else:
                memo.append(memo[i-2] + memo[i-3])
        return memo[-1]
