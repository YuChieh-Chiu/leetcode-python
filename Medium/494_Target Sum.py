class Solution:
    def __init__(self) -> None:
        # {'index': 'current_sum'}: 紀錄到目前這層時，相同 current_sum 的有哪些
        self.memo = {}

    def recursionAndMemo(self, index: int, current_sum: int, nums: List[int], target: int) -> int:
        # 終止條件：處理完 nums 中的所有數字
        if index == len(nums):
            return 1 if current_sum == target else 0

        # 檢查記憶表
        if (index, current_sum) in self.memo:
            return self.memo[(index, current_sum)]
        
        # 不在記憶表中，遞迴更新值
        equal_to_target_from_add = self.recursionAndMemo(index + 1, current_sum + nums[index], nums, target)
        equal_to_target_from_subtract = self.recursionAndMemo(index + 1, current_sum - nums[index], nums, target)

        # 將遞迴結果紀錄記憶表中
        self.memo[(index, current_sum)] = equal_to_target_from_add + equal_to_target_from_subtract

        return self.memo[(index, current_sum)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Thought:
        - Problem description:
            - We need to use all integers in the array `nums`, each with one of the symbols `+` or `-`, to construct an expression that equals the integer `target`.
        - Idea:
            - Use recursion to explore all possible results and check if the result equals the target.
                - Key Concepts:
                    1. The base condition at the deepest level should return a "check result." If the result equals the target, return 1; otherwise, return 0.
                    2. Use memoization to store the results of each level as a combination of `(index, current_sum)` and aggregate the counts from recursive calls. This allows the total count to be obtained when the function is called from the top level.
        - Steps:
            (1) Initialize `self.memo = {}` to store the count results for each level.
            (2) Define a recursive function with memoization that satisfies the above Key Concepts.
            (3) Call the recursive function to return the final result.
        - Topics:
            - Dynamic Programming, Memoization, Recursion
        """
        return self.recursionAndMemo(0, 0, nums, target)
