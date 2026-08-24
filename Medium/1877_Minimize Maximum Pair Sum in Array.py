class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        """
        Thought:
        - Goal: Minimize the maximum pair sum formed by pairing all elements in an array of even length.
        - Idea: Sort the array and pair the smallest available element with the largest available element (Greedy strategy with two pointers).
        - Steps:
            1. Sort the input array `nums` in non-decreasing order.
            2. Iterate through the first half of the array using index `i`.
            3. Pair `nums[i]` with its corresponding element from the end, `nums[n - 1 - i]`.
            4. Track and return the maximum pair sum found.
        - Time Complexity: O(N log N) where N is the length of `nums`.
        - Space Complexity: O(1) or O(N) depending on Python's Timsort implementation.
        """

        nums.sort()

        n = len(nums)
        max_pair_sum = 0

        for i in range(n//2):
            max_pair_sum = max(max_pair_sum, nums[i] + nums[n-1-i])

        return max_pair_sum
