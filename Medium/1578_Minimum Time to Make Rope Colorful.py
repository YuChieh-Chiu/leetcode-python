class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        """
        Goal:
            - Remove adjacent balloons with the same color to make the rope colorful.
            - Minimize the total time needed to remove balloons.
        Idea:
            - Group consecutive balloons of the same color into segments.
            - For each segment, keep the balloon with the maximum removal time and remove all others (this minimizes the cost for that segment).
            - The cost for each segment is: (sum of all removal times) - (max removal time).
        Steps:
            1. Iterate through the balloons and track consecutive same-color segments.
            2. For each segment, accumulate the total removal time and track the maximum.
            3. When the color changes, add the segment cost (total - max) to the result.
            4. Handle the final segment after the loop ends.
        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - only using a constant amount of extra space
        """
        total_cost = 0
        current_color = colors[0]
        segment_sum = neededTime[0]
        segment_max = neededTime[0]
        
        for i in range(1, len(colors)):
            if colors[i] == current_color:
                segment_sum += neededTime[i]
                segment_max = max(segment_max, neededTime[i])
            else:
                total_cost += segment_sum - segment_max
                current_color = colors[i]
                segment_sum = neededTime[i]
                segment_max = neededTime[i]
        
        # Handle the last segment
        total_cost += segment_sum - segment_max
        
        return total_cost
