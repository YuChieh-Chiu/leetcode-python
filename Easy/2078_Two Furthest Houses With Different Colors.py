class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        """
        Thought:
        - Goal: Find the maximum distance between two houses with different colors.
        - Idea: To maximize the distance, at least one of the target houses MUST be at the boundary of the array (either the leftmost or the rightmost house). We can find the answer by checking these two fixed points.
        - Steps:
            1. Fix the leftmost house (index 0) and iterate backwards from the end of the array. Find the first house with a different color, record the distance, and break the loop.
            2. Fix the rightmost house (index n-1) and iterate forwards from the beginning of the array. Find the first house with a different color, record the distance, and break the loop.
            3. Return the maximum value between the two recorded distances.
        - Time Complexity: O(n), where n is the length of the colors array.
        - Space Complexity: O(1).
        """
        n = len(colors)
        max_dist = 0

        # Fix the leftmost house, scan from the right
        for i in range(n - 1, 0, -1):
            if colors[i] != colors[0]:
                max_dist = max(max_dist, i)
                break

        # Fix the rightmost house, scan from the left
        for i in range(n - 1):
            if colors[i] != colors[-1]:
                max_dist = max(max_dist, (n - 1) - i)
                break

        return max_dist
