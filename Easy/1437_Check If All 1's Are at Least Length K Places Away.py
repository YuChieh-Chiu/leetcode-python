class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        """
        Thought:
        - Goal: Determine if all 1's in the binary array are at least k places apart from each other.
        - Idea:
            - Traverse the array from left to right and track the position of the last 1 encountered.
            - When a 1 is found, check if the distance from the previous 1 is at least k.
            - If any pair of 1's violates the constraint, return False immediately.
        - Steps:
            1. Initialize last_one_index to -inf to handle the first 1 naturally.
            2. Iterate through the array with enumeration.
            3. When encountering a 1:
                - Check if the distance from last_one_index is greater than k.
                - If not, return False immediately.
                - Update last_one_index to current index.
            4. If loop completes without violations, return True.
        - Time Complexity: O(n), where n is the length of nums. We traverse the array once.
        - Space Complexity: O(1), only using constant extra space for variables.
        """
        last_one_index = -float('inf')
        
        for idx, num in enumerate(nums):
            if num == 1:
                if idx - last_one_index <= k:
                    return False
                last_one_index = idx
        
        return True
