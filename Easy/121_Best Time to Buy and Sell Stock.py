class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Thought:  
        - Problem Information:  
            - Given an array `prices` where `prices[i]` represents the price of a stock on the i-th day.  
        - Goal:  
            - Maximize profit by choosing a single day to buy and a later day to sell.  
            - If no profit can be achieved, return `0`.
        - Concept:  
            - Traverse the array `prices` to calculate the profit by comparing the current price with the minimum price seen so far, and find the maximum profit.
        - Steps:  
            1. Initialize `min_price` to infinity and `max_profit` to 0.
            2. Traverse the array `prices`. For each price:
                - Update the current minimum price using `min(min_price, price)`.
                - Update the maximum profit using `max(max_profit, price - min_price)`.
            3. Return the final `max_profit`.
        """

        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
