class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        """
        Thought:
        - Goal: Find the minimum total cost to reach step n from step 0.
        - Idea: 
        Use 1D Dynamic Programming. To arrive at step i, we can only transition from 
        step i-1, i-2, or i-3. The cost to reach step i is costs[i] plus the minimum of 
        (dp[prev_step] + (i - prev_step)^2) across all valid previous steps.
        - Steps:
        1. Pad `costs` with 0 at index 0 so that step indices match array indices (0 to n).
        2. Initialize a DP table where dp[0] = 0 and other entries are initialized to infinity.
        3. Iterate through step i from 1 to n:
            - Check possible previous steps (i-1, i-2, i-3).
            - Calculate transition cost as dp[prev] + (i - prev)^2.
            - Set dp[i] = costs[i] + min(valid transitions).
        4. Return dp[n].
        - Time Complexity: O(n)
        - Space Complexity: O(n)
        """

        costs = [0] + costs
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(1, len(costs)):
            cost_3_step = dp[i-3] + 9 if i >= 3 else float('inf')
            cost_2_step = dp[i-2] + 4 if i >= 2 else float('inf')
            cost_1_step = dp[i-1] + 1
            
            dp[i] = costs[i] + min(cost_3_step, cost_2_step, cost_1_step)

        return dp[n]
