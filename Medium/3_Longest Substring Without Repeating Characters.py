class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        thought:
        - we should get the longest `substring` without repeated characters
        - find substring -> we can try to use `sliding window`
        - the key point for us is to traverse the string `s` and make sure that the substring without repeated characters
            (1) extend window first
            (2) check i, the latest character repeats or not
            (3) traverse from left_border to i-1 to find k, the index of the repeated character and cut off the part before k (include k)
        """
        # record the number of characters in `sliding window`
        # length of `char_cnt` = 256 because the english letters, digits, symbols, and spaces is between 0~255
        char_cnt = [0]*256 
        longest_substring = 0
        left_border = 0
        for idx, char in enumerate(s):
            ord_char = ord(char)
            char_cnt[ord_char] += 1
            if char_cnt[ord_char] > 1: # repeats
                for i in range(left_border, idx):
                    if ord(s[i]) == ord_char: # find the repeat element and cut off the part before it (include it)                        
                        left_border = i + 1
                        break
            substring_length =  (idx - left_border + 1)
            if substring_length > longest_substring:
                longest_substring = substring_length
        return longest_substring
