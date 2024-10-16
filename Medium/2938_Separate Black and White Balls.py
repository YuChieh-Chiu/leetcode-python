class Solution:
    def minimumSteps(self, s: str) -> int:
        """
        thought:
        - From the problem description, we can infer that:
            (1) `1` and `0` represent black and white balls respectively.
            (2) The string `s` is a 0-indexed binary string.
            (3) We can only swap two adjacent balls.
        - Our goal is to calculate the minimum number of steps required to group all the black balls to the right and all the white balls to the left.
        - It appears that we need to use the `two pointers` algorithm to traverse the string `s` and locate two elements simultaneously each time.
        - Note that we can only swap adjacent balls, so our target is to ensure all elements to the left of the left pointer are `0`.
        - Therefore, we can follow these steps:
            (1) Initialize `left` to 0, `right` to 1, and `swap` to 0.
            (2) Convert the string into a list because strings are immutable.
            (3) If the value at the `left` index is `0`, move the pointers forward.
            (4) If the value at the `left` index is `1` and the value at the `right` index is `0`, swap them. After swapping, add `(right - left)` to `swap`, and increment both `left` and `right` by 1.
            (5) In other cases, keep `left` fixed and increment `right` to traverse further to the right.
            (6) Continue until `right` reaches the length of `s`, then end the iteration and return the value of `swap`.
        """
        swap = 0
        left = 0
        right = 1
        s = [int(char) for char in s]
        while right < len(s):
            if s[left] == 0:
                left += 1
                right += 1
            else:
                if s[left] > s[right]:
                    s[left] = 0
                    s[right] = 1
                    swap += (right-left)
                    left += 1
                    right += 1
                else:
                    right += 1
        return swap
