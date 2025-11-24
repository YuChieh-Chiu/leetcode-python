class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        """
        Thought:       
        - Goal: Given a binary array nums, where x_i represents the decimal value of the subarray nums[0..i], determine whether each x_i is divisible by 5 and return a boolean array.
        - Idea:
            - Use iterative calculation to build each x_i from x_(i-1). Since appending a bit to a binary number is equivalent to shifting left (multiply by 2) and adding the new bit, we can compute: x_i = x_(i-1) * 2 + nums[i]
            - To prevent overflow and improve performance, we only track the remainder modulo 5, as (a * 2 + b) % 5 == ((a % 5) * 2 + b) % 5.
        - Steps:
            1. Initialize current remainder as 0
            2. For each bit in nums:
               - Update current = (current * 2 + bit) % 5
               - Check if current == 0 (divisible by 5)
               - Append result to answer list
            3. Return the answer list        
        - Time Complexity: O(n)
            - Single pass through the array
            - Each operation (multiply, add, modulo, append) is O(1)
        - Space Complexity: O(n)
            - Output array stores n boolean values
            - Only O(1) extra space for variables if output is not counted
        """
        current = 0
        answer = []
        
        for num in nums:
            current = (current * 2 + num) % 5
            answer.append(current == 0)
        
        return answer
