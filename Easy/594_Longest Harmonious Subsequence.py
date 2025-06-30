class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """
        Thought:
        - Goal: get the length of the longest harmonious subsequence.
        - Definition of harmonious subsequence: a subsequence where the difference between its maximum value and its minimum value is exactly 1.
        - Idea:
            - A harmonious subsequence can only contain two distinct values that differ by exactly 1
            - Use dictionary to count the frequency of each value in the array
            - For each value num, only check if num+1 exists to avoid duplicate counting of pairs
            - If num+1 exists, the harmonious subsequence length = count[num] + count[num+1]
        - Steps:
            1. Count the frequency of each value in the array using a dictionary
            2. Initialize longest to 0 to track the maximum harmonious subsequence length
            3. Iterate through each value num in the dictionary
            4. Check if num+1 also exists in the dictionary
            5. If num+1 exists, calculate count[num] + count[num+1] and update longest
            6. Return the longest harmonious subsequence length
        """

        longest = 0
        val_cnt = {}
        for num in nums:
            if num in val_cnt:
                val_cnt[num] += 1
            else:
                val_cnt[num] = 1

        for num in val_cnt.keys():
            if num+1 in val_cnt:
                length = val_cnt[num] + val_cnt[num+1]
                longest = max(longest, length)
        
        return longest
