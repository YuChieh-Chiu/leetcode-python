class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        thought: 
        1. 出現偶數次的直接加上去
        2. 出現奇數次的加上該數字減一次，再在最後加一
        """
        s_cnt = {}
        for c in s:
            if c in s_cnt:
                s_cnt[c] += 1
            else:
                s_cnt[c] = 1
        length = 0
        odd_exist = False
        for k, v in s_cnt.items():
            if v % 2 == 0:
                length += v
            else:
                length += (v-1)
                odd_exist = True
        if odd_exist:
            length += 1
        return length
