class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """
        Thought:
        - Goal: Find the minimum total number of moves (+1 operations) to make all elements in nums equal.
        - Idea: Since elements can only be increased, every element must eventually equal the maximum value in the array. The minimum moves required equals the sum of differences between each element and the maximum.
        - Steps:
            1. Find the maximum value in `nums`.
            2. Compute the difference between each element and this maximum value.
            3. Sum all differences and return the result.
        - Time Complexity: O(n), where n is the length of `nums`. Finding the maximum takes O(n), and iterating through the list to calculate differences also takes O(n).
        - Space Complexity: O(1), auxiliary space is constant since we only keep track of the maximum value and the running total.
        """

        maximum = max(nums)

        moves = 0
        for num in nums:
            moves += maximum - num

        return moves
