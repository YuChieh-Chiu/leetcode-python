class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        """
        Thought:
        - Goal: Calculate the sum of the squares of distinct element counts for all possible contiguous subarrays of `nums`.
        - Idea: Use a nested loop to generate every subarray starting at index `i` and ending at index `j`. Maintain a hash set (`seen`) for each starting position `i` to dynamically track unique elements as the subarray expands.
        - Steps:
            1. Initialize `total_sum` to 0 to accumulate the final result.
            2. Iterate through each starting index `i` from 0 to `len(nums) - 1`.
            3. Initialize an empty set `seen` for the current starting index `i`.
            4. Iterate through each ending index `j` from `i` to `len(nums) - 1`:
                a. Add `nums[j]` to `seen`.
                b. Add the square of the current set size (`len(seen) ** 2`) to `total_sum`.
            5. Return `total_sum`.
        - Time Complexity: O(N^2), where N is the length of `nums`, due to the nested loops iterating over all subarrays. Set insertions and length checks take O(1) average time.
        - Space Complexity: O(N), as the `seen` set stores at most N unique elements in the worst case.
        """

        total_sum = 0
        for i in range(len(nums)):
            seen = set()
            for j in range(i, len(nums)):
                seen.add(nums[j])
                total_sum += len(seen) ** 2

        return total_sum
