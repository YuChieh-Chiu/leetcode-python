class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        thought:
        - this is one of the classic `two pointers` problems. The idea is to start by choosing `vertical lines` from the two outermost sides and gradually move inward, replacing the lines step by step to find the two `vertical lines` that provide the maximum capacity.
        - therefore, we can follow these steps:
            (1) set the leftmost and rightmost `vertical lines`.
            (2) calculate the capacity between two `vertical lines`.
            (3) after each capacity calculation, remove the SHORTER `vertical line` and continue moving inward until the two `vertical lines` overlap.
                # the reason that we can do the operation in (3) is because the capacity means `the distance between two vertical lines * height of the SHORTER vertical line`, when one of the vertical lines is fixed as the SHORTER one, it is impossible to find a larger capacity by moving inward
            (4) return the maximum capacity.
        """
        max_area = 0
        left_border = 0
        right_border = len(height)-1
        while left_border != right_border:
            area = min(height[left_border], height[right_border]) * (right_border-left_border)
            if area > max_area:
                max_area = area
            if height[left_border] > height[right_border]:
                right_border -= 1
            else:
                left_border += 1
        return max_area
