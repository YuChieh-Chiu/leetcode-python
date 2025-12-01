class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        """
        Thought:
        - Goal: Find the minimum cost to purchase all candies
        - Idea: 
            - Use greedy algorithm. The key insight is that we should maximize the value of free candies. 
            - Since the free candy must have a cost ≤ min(two paid candies), we should sort candies by price in descending order and process them in groups of 3. This ensures we always get the most expensive eligible candy for free.
        - Steps:
            1. Sort the cost array in descending order
            2. Iterate through the array with step size 3
            3. For each group, add the cost of first two candies (most expensive)
            4. Skip the third candy in each group (it's free)
            5. Return the total cost
        - Time Complexity: O(n log n) due to sorting
        - Space Complexity: O(1) - only use constant extra space for variables
        """
        cost.sort(reverse=True)
        total_cost = 0
        
        for i in range(0, len(cost), 3):
            total_cost += cost[i]
            if i + 1 < len(cost):
                total_cost += cost[i + 1]
        
        return total_cost
