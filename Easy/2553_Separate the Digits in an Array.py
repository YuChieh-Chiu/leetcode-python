class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        """
        Thought:
        - Goal: Extract and separate the individual digits of each integer in the given array, maintaining their original order.
        - Idea: Iterate through each integer in the array, convert it to a string to easily access its individual characters (digits), convert each character back to an integer, and collect them into a new result array.
        - Steps:
            1. Initialize an empty list `answer` to store the result.
            2. Iterate through each integer `num` in the `nums` array.
            3. Convert `num` to a string and iterate through each character `char`.
            4. Cast `char` back to an integer and append it to `answer`.
            5. Return the `answer` array.
        - Time Complexity: O(N), where N is the total number of digits across all integers in the array.
        - Space Complexity: O(N), where N is the total number of digits, as we need to store them in the result array.
        """
        answer = []

        for num in nums:
            for char in str(num):
                answer.append(int(char))

        return answer
