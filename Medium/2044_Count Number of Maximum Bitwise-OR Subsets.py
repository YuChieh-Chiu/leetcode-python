class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        """
        # Bitmask Approach (I used)
        Thought:
        - Goal: Find the maximum possible bitwise OR and count subsets achieving it
        - Constraint: Only count non-empty subsets
        - Idea: Use bitmask to represent all possible subset combinations, where each bit indicates whether an element is selected
        - Steps:
            1. Calculate the maximum possible OR by combining all elements
            2. Iterate through all possible bitmasks from 1 to 2^n-1 (excluding empty set)
            3. For each mask, check each bit to determine which elements to include in the subset
            4. Calculate the OR value of the current subset and increment counter if it equals the maximum OR
        - Time Complexity: O(2^n)

        # Recursive Approach
        Thought:
        - Goal: Find the maximum possible bitwise OR and count subsets achieving it
        - Constraint: Only count non-empty subsets
        - Idea: Use recursion to explore all possible subset combinations by deciding whether to include each element or not
        - Steps:
            1. Calculate the maximum possible OR by combining all elements
            2. Use recursive function with parameters: current index, current OR value, and whether any element has been selected
            3. For each element, make two recursive calls: one including the element and one excluding it
            4. Count valid subsets when reaching the end if they are non-empty and equal to maximum OR
        - Time Complexity: O(2^n)
        """
        # step1: calculate max OR
        maxOR = 0
        for num in nums:
            maxOR |= num

        # step2. find max OR subsets by bitmask
        count = 0
        n = len(nums)
        for mask in range(1, 2**n):
            currentOR = 0
            for i in range(n):
                if (mask & (1 << i)) != 0:
                    currentOR |= nums[i]
            if currentOR == maxOR:
                count += 1

        return count
