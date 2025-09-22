# from collections import Counter

# class Solution:
#     def maxFrequencyElements(self, nums: List[int]) -> int:
#         """
#         Thought:
#         - Goal: Find the total count of elements that have the maximum frequency in the array
#         - Idea: Count frequencies of all elements, identify the maximum frequency, then sum up the total occurrences of all elements with that maximum frequency
#         - Steps:
#             1. Count the frequency of each element using Counter
#             2. Sort elements by frequency in descending order to find the maximum frequency
#             3. Filter elements with maximum frequency and calculate their total count
#         - Time Complexity: O(n log n) due to sorting operation
#         - Space Complexity: O(n) for storing frequency counts and sorted results
#         """
#         num_cnt = Counter()

#         for num in nums:
#             num_cnt[num] += 1

#         sorted_cnt = sorted(num_cnt.items(), key=lambda x:x[1], reverse=True)

#         max_cnt = [cnt for (_, cnt) in sorted_cnt if cnt == sorted_cnt[0][1]]

#         return len(max_cnt) * max_cnt[0]



from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        """
        Thought:
        - Goal: Find the total count of elements that have the maximum frequency in the array
        - Idea: Count frequencies of all elements, find the maximum frequency value, then sum up all frequency values that equal the maximum
        - Steps:
            1. Use Counter to record the frequency of each positive integer
            2. Use max() to get the maximum frequency value
            3. Sum up all frequency values that match the maximum frequency
        - Time Complexity: O(n)
        - Space Complexity: O(n)
        """
        num_cnt = Counter()

        for num in nums:
            num_cnt[num] += 1

        max_value = max(num_cnt.values())

        return sum([val for (_, val) in num_cnt.items() if val == max_value])
