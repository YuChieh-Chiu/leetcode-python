class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        thought:
        - we want to sort the list first, and then check whether sort_list[i] equals to  list[i] or not
        - sort in ascending order
        - check the value index by index
        """
        diff_cnt = 0
        expected = sorted(heights, reverse=False)
        for (height_i, expected_i) in zip(heights, expected):
            if height_i == expected_i:
                pass
            else:
                diff_cnt += 1
        return diff_cnt
