class Solution:
    def calc_gcd(self, a: int, b:int) -> int:
        if b == 0: # 已輾轉相除到取得最大公因數了
            return a

        return self.calc_gcd(b, a%b) # 核心概念：a,b 的最大公因數就是 b 跟 a 除以 b 的餘數的最大公因數
    def findGCD(self, nums: List[int]) -> int:
        """
        Thought:
        - Goal: Find the Greatest Common Divisor (GCD) of the smallest and largest numbers in a given integer array.
        - Idea: Identify the boundary values (min and max) of the array and then apply the Euclidean algorithm via the math library to find their GCD.
        - Steps:
            1. Scan the array to find the minimum value.
            2. Scan the array to find the maximum value.
            3. Compute and return the GCD of these two values using math.gcd().
        - Time Complexity: O(n), where n is the length of nums.
            - original: O(n) + O(n) + O(log(min(a,b)))
        - Space Complexity: O(1).
        """
        max_val = max(nums)
        min_val = min(nums)

        return self.calc_gcd(max_val, min_val)
