class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        """
        Thought:
        - Goal: Find the minimum time to visit all points in the given order on a 2D plane.
        - Idea: In each step, you can move horizontally, vertically, or diagonally. The distance between two points (x0, y0) and (x1, y1) under these rules is the Chebyshev distance, which is defined as max(|x1 - x0|, |y1 - y0|).
        - Steps:
            1. Initialize a variable `total_time` to 0.
            2. Iterate through the points in pairs (current point and next point).
            3. For each pair, calculate the maximum of the absolute differences of their x and y coordinates.
            4. Accumulate this value into `total_time`.
            5. Return the total accumulated time.
        - Time Complexity: O(n), where n is the number of points in the list.
        - Space Complexity: O(1), as we only use a constant amount of extra space for the total time.
        """
        total_time = 0

        for (x0, y0), (x1, y1) in zip(points, points[1:]):
            total_time += max(abs(x1 - x0), abs(y1 - y0))

        return total_time
