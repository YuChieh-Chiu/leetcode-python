class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """
        thought:
        - our target is to turn `t` into `ta`, which is an `Anagram` of `s`
        - because `an Anagram of a string is a string that contains the same characters with a different (or the same) ordering.`, all we need to do is calculate how many characters are different between `t` and `s`
        """
        # record the number of steps
        cnt = 0
        # get the number of each character in `s`
        s_dict = {}
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        # Get the count of each character missing in `t` from `s`
        for char in t:
            if char in s_dict:
                s_dict[char] -= 1
        # calculate the total steps
        for _, v in s_dict.items():
            cnt += (v if v > 0 else 0)
        return cnt
