class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        Thought:
        - Goal: Ensure that all elements in the array are distinct.
        - Constraint: The only allowed operation is as follows:  
            - Remove 3 elements from the beginning of the array, or all remaining elements if fewer than 3 remain.
        - Idea:  
            - If all elements in the array are distinct, the length of the array is equal to the length of its set.
        - Steps:  
            1. Initialize a variable `removal` to 0 to track the number of removal operations.  
            2. Use a while loop to repeatedly check whether the length of the array equals the length of its set:  
                - If unequal: This means there are still duplicate values. Increment `removal` and remove 3 elements from the beginning of the array.  
                - If equal: Exit the loop.  
            3. Return `removal`.
        """
        
        removal = 0
        
        while len(set(nums)) != len(nums):
            removal += 1
            try:
                nums = nums[3:]
            except:
                nums = []

        return removal
