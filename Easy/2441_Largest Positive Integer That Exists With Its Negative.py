class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        """
        Thought:
        - Goal: Find the largest positive integer such that its negative counterpart (the number * -1) also exists in nums. If no such number exists, return -1.
        - Idea:
        1. Initialize largest_positive_integer to -1
        2. Create a hash set from nums for O(1) lookup time
        3. Iterate through nums and for each number, check if its negative counterpart exists in the set
        4. Keep track of the maximum positive number that satisfies the condition
        - Steps:
        1. Initialize largest_positive_integer to -1
        2. Create set_nums = set(nums) for fast lookup
        3. Iterate through nums. For each number:
            - Check if the number * -1 exists in set_nums
            - If it exists and the number is greater than largest_positive_integer, update largest_positive_integer
        4. Return largest_positive_integer
        - Time: O(n), Space: O(n)

        Other Solutions:
        1. Sort + Early Break Approach:
        - Time: O(n log n), Space: O(n)
        - Sort nums in descending order, iterate from largest to smallest positive numbers
        - Use set for O(1) lookup, break immediately when first match is found
        - Advantage: Early termination saves time in best cases

        2. Two Pointers Approach:
        - Time: O(n log n), Space: O(1)
        - Sort the array, use left pointer at start (negative numbers) and right pointer at end (positive numbers)
        - Compare absolute values and move pointers accordingly
        - Advantage: O(1) extra space usage, but slower due to sorting requirement
        - Trade-off: Space-efficient but time-inefficient compared to hash set approach
        """
        largest_positive_integer = -1

        set_nums = set(nums)

        for num in nums:
            if num * (-1) in set_nums:
                if num > largest_positive_integer:
                    largest_positive_integer = num
                # break

        return largest_positive_integer
