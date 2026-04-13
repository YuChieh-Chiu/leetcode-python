class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        """
        Thought:
        - Goal: Find the minimum absolute distance between the index `start` and any index `i` where `nums[i] == target`.
        - Idea: Traverse the array while keeping track of the minimum distance encountered so far whenever we find an element that matches the `target`.
        - Steps:
            1. Initialize a variable `min_abs` to infinity (`float('inf')`) to keep track of the minimum distance.
            2. Iterate through the array `nums` using `enumerate` to access both the index `i` and the value `num`.
            3. For each element, check if `num` equals the `target`.
            4. If it does, calculate `abs(i - start)` and update `min_abs` with the smaller value between the current `min_abs` and the newly calculated distance.
            5. Return the final `min_abs`.
        - Time Complexity: O(N)
        - Space Complexity: O(1)
        """

        min_abs = float('inf')

        for i, num in enumerate(nums):
            if num == target:
                min_abs = min(min_abs, abs(i - start))

        return min_abs
