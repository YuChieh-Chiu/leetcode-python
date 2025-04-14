class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        """
        Thought:
        - Goal: Given an array of integers `arr` and three integers `a`, `b`, and `c`, find the number of good triplets.
        - Definition of good triplets:  
            A triplet (i, j, k) is considered good if:  
            1. 0 <= i < j < k < len(arr)
            2. |arr[i] - arr[j]| <= a
            3. |arr[j] - arr[k]| <= b 
            4. |arr[i] - arr[k]| <= c
        - Idea:  
            - We need to iterate through `arr` with triple-nested loops to explore all combinations of (i, j, k) and check whether they form good triplets.
        - Steps:  
            1. Initialize a counter `goodTriplets` to 0 to track the number of good triplets.  
            2. Use triple-nested loops to evaluate all possible triplets:  
                - Ensure that the loop ranges satisfy condition (1) of the good triplet definition.  
                - In the innermost loop, check whether the elements at indices i, j, and k satisfy conditions (2) to (4).  
                - If all conditions are satisfied, increment `goodTriplets` by 1.  
            3. Return `goodTriplets`.
        - Time Complexity: O(n^3)
        - Space Complexity: O(1)
        """
        
        goodTriplets = 0
        length = len(arr)

        for i in range(length-2):
            for j in range(i+1, length-1):
                for k in range(j+1, length):
                    if (abs(arr[i]-arr[j]) <= a) and (abs(arr[j]-arr[k]) <= b) and (abs(arr[i]-arr[k]) <= c):
                        goodTriplets += 1
                    
        return goodTriplets
