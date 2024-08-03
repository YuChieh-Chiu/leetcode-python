class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        """
        thought:
        - two arrays can be made equal by reversing subarrays only if they contain the same elements.
        - therefore, we can follow these steps:
            (1) sort both arrays in ascending order.
            (2) compare the two arrays element by element. If any element does not match, return False. Otherwise, return True.
        """
        target = sorted(target)
        arr = sorted(arr)
        for t, a in zip(target, arr):
            if t != a:
                return False
        return True
