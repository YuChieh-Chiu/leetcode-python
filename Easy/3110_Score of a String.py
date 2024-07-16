class Solution:
    def scoreOfString(self, s: str) -> int:
        """
        thought:
        - we need to calculate and sum the absolute differences of the ASCII values between the i-th and (i-1)-th characters.
        - therefore, we can follow these steps:
            (1) calculate the ASCII value of the 0th character and set it as `last_ord`.
            (2) for the 1st to the N-th characters, when calculating the ASCII value of the i-th character, get the ASCII value of the i-th character (`this_ord`), subtract the ASCII value of the (i-1)-th character (`last_ord`) from it, take the absolute value, and update `last_ord` to `this_ord`.
            (3) the sum of the results from the loop in step (2) is the answer.
        """
        score = 0
        last_ord = ord(s[0])
        for char in s[1:]:
            this_ord = ord(char)
            score += abs(this_ord-last_ord)
            last_ord = this_ord
        return score
