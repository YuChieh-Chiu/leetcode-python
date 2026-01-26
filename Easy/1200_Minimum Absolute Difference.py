class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        """
        Thought:
        - Goal: Find all pairs of integers from a distinct array that have the minimum absolute difference.
        - Idea: Sorting the array allows us to find the minimum difference by only comparing adjacent elements, as the smallest difference must exist between neighbors in a sorted sequence.
        - Steps:
            1. Sort the input array in ascending order.
            2. Iterate through the sorted array and calculate the difference between adjacent elements.
            3. If a new minimum difference is found, clear the result list and add the current pair.
            4. If the difference matches the current minimum, append the pair to the result list.
        - Time Complexity: O(n log n) due to the sorting step.
        - Space Complexity: O(n) for the output list.
        """
        min_diff = float('inf')
        res = []

        arr.sort()  # 原地排序節省空間

        # 使用 range 避免切片產生的額外空間開銷
        for i in range(len(arr) - 1):
            a, b = arr[i], arr[i + 1]
            diff = b - a
            
            if diff < min_diff:
                min_diff = diff
                res = [[a, b]]
            elif diff == min_diff:
                res.append([a, b])
                
        return res
