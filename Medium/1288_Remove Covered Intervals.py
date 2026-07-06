class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """
        Thought:
        - Goal: Remove all sub-intervals that are completely covered by another interval, and return the count of remaining intervals.
        - Idea (Original - Intuitive): 
            Compare every pair of intervals using nested loops. If an interval is covered by another, increment a counter. This approach works but requires O(n^2) time.
        - Idea (Advanced - Optimal): 
            Sort the intervals first. By sorting start times in ascending order and end times in descending order (for ties), we guarantee that any subsequent interval starts at the same time or later. Therefore, an interval is completely covered if and only if its end time is less than or equal to the maximum end time (`max_end`) seen so far.
        - Steps (Advanced):
            1. Sort `intervals` in-place using `key=lambda x: (x[0], -x[1])`.
            2. Initialize an `uncovered` counter to 1 and a `max_end` variable to the end time of the very first interval.
            3. Iterate through the rest of the intervals.
            4. If the current interval's end is strictly greater than `max_end`, it is not covered. Increment the `uncovered` counter and update `max_end`.
            5. Return the final `uncovered` count.
        - Time Complexity: O(n log n). Sorting the array takes O(n log n) time, and the subsequent single-pass iteration takes O(n) time. The overall complexity is dominated by the sorting step.
        - Space Complexity: O(n). Python's built-in sorting algorithm (Timsort) requires up to O(n) auxiliary space in the worst case.
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))

        uncovered = 1
        max_end = intervals[0][1]

        for start, end in intervals[1:]:
            if end > max_end:
                max_end = end
                uncovered += 1

        return uncovered
