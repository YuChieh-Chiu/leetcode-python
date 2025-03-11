class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        Thought:
        - Goal:
            - Return the number of substrings in string `s` that contain at least one occurrence of all three characters: 'a', 'b', and 'c'.
            - Note that `s` consists only of the characters 'a', 'b', and 'c'.
        - Idea:
            - At each position in the string, find the first occurrence of 'a', 'b', and 'c' starting from that position.
            - Once found, all substrings extending beyond this position will be valid substrings, so we can count them directly.
        - Steps:
            1. Define `length` as the length of the string `s`.
            2. Initialize a counter `cnt` to 0.
            3. Iterate through the string `s`:
                - At each position, use `str.find(val, idx)` to find the first occurrence of 'a', 'b', and 'c' starting from that index.
                - Use `max()` to determine the maximum index among the three found positions. Every substring extending beyond this index is a valid substring, so we can count them as `length - max_loc`.
                - Note: If `str.find()` returns `-1` for any character, it means that character is missing in the remaining substring, and we should exclude such cases.
            4. Return `cnt`.
        """
        length = len(s)
        cnt = 0

        for i in range(length):
            loc_a = s.find("a", i)
            loc_b = s.find("b", i)
            loc_c = s.find("c", i)
            if loc_a >= 0 and loc_b >= 0 and loc_c >= 0:
                max_loc = max(loc_a, loc_b, loc_c)
                cnt += length - max_loc

        return cnt
