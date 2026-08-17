class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        """
        Thought:
        - Goal: Determine if there exists a sub-pattern of length `m` that repeats consecutively `k` or more times in `arr`.
        - Idea: If a pattern of length `m` repeats `k` times consecutively, each element at index `i` must match the element at index `i + m`. We can maintain a counter `count` that increments when `arr[i] == arr[i + m]` and resets to `0` on mismatch. A valid pattern is confirmed when `count` reaches `(k - 1) * m`.
        - Steps:
            1. Calculate the required total matches: `target = (k - 1) * m`.
            2. Iterate through `arr` from index `0` up to `len(arr) - m - 1`.
            3. If `arr[i] == arr[i + m]`, increment `count` by 1. If `count == target`, return `True`.
            4. If `arr[i] != arr[i + m]`, reset `count` to `0`.
            5. Return `False` if the loop finishes without meeting the target.
        - Time Complexity: O(N), where N is the length of `arr`.
        - Space Complexity: O(1), auxiliary memory used is constant.
        """
        target = (k-1) * m
        count = 0
       
        for i in range(len(arr)-m):
            if arr[i] == arr[i+m]:
                count += 1
                if count == target:
                    return True
            else:
                count = 0

        return False
