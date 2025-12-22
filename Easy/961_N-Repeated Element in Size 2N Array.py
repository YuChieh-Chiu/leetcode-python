class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        """
        Thought:
        - Goal: Find the element that repeats n times in a 2n-length array.
        - Idea: Given n+1 unique elements, only one element is repeated while all others 
                appear exactly once. Therefore, the first element encountered twice is our answer.
        - Steps:
            1. Create a set 'seen' to store elements already visited.
            2. Iterate through 'nums'.
            3. If an element is in 'seen', return it immediately.
            4. Otherwise, add it to 'seen'.
        - Time Complexity: O(N), where N is the length of nums.
        - Space Complexity: O(N), specifically O(N/2 + 1) to store unique elements.
        """
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)



# class Solution:
#     def repeatedNTimes(self, nums: List[int]) -> int:
#         """
#         Thought:
#         - Goal: Find the element that repeats n times in a 2n-length array.
#         - Idea: Count the frequency of every element using a hash map and then identify 
#                  the one that matches the target count n.
#         - Steps:
#             1. Calculate the target frequency n = len(nums) // 2.
#             2. Initialize a dictionary 'count_dict' to store frequencies.
#             3. Iterate through 'nums' to populate the dictionary.
#             4. Iterate through the dictionary to find the key with value n.
#         - Time Complexity: O(N), where N is the length of nums (two-pass).
#         - Space Complexity: O(N), as the dictionary stores n+1 unique elements.
#         """
#         n = len(nums) // 2

#         count_dict = {}

#         for num in nums:
#             if num in count_dict:
#                 count_dict[num] += 1
#             else:
#                 count_dict[num] = 1

#         for key, val in count_dict.items():
#             if val == n:
#                 return key
