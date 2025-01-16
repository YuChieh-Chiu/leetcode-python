class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Thought:
        - Goal:
            - First, obtain all the XOR combinations from `nums1` and `nums2`, store them in `nums3`, and then compute the XOR result of all values in `nums3`.
        - Definition:
            - XOR: Convert two numbers `a` and `b` into binary representation, compare each bit, where matching bits result in 0, differing bits result in 1. Finally, convert the binary result back to decimal.
                - In Python, XOR can be computed using `a ^ b`.
                - Properties of XOR:
                    1. If `a = b`, then `a ^ b = 0`
                    2. If `a = 0`, then `a ^ b = b`
                    3. Commutative property: `a ^ (b ^ c) = (a ^ b) ^ c`
        - Idea:
            Example:
                nums1 = [a, b, c], nums2 = [x, y, z]
            Solution:
                final_xor 
                = (a ^ x) ^ (a ^ y) ^ (a ^ z) ^ (b ^ x) ^ (b ^ y) ^ (b ^ z) ^ (c ^ x) ^ (c ^ y) ^ (c ^ z)
                = (a ^ a ^ a) ^ (b ^ b ^ b) ^ (c ^ c ^ c) ^ (x ^ x ^ x) ^ (y ^ y ^ y) ^ (z ^ z ^ z)
                = (0 ^ a) ^ (0 ^ b) ^ (0 ^ c) ^ (0 ^ x) ^ (0 ^ y) ^ (0 ^ z)
                = a ^ b ^ c ^ x ^ y ^ z
        - Key Concept:
            - According to the properties of XOR, the problem can be simplified: determine whether the length of the list is odd or even, and perform the corresponding simplification.
        - Steps:
            1. Initialize `final_xor` to 0.
            2. Check the lengths of `nums1` and `nums2`:
                - If both `nums1` and `nums2` have even lengths, the XOR of all values will result in 0, so `final_xor` will be 0.
                - If `nums1` has an even length and `nums2` has an odd length, the XOR of all values in `nums2` will be 0, so `final_xor` will be the XOR of all values in `nums1`.
                - If `nums1` has an odd length and `nums2` has an even length, the XOR of all values in `nums1` will be 0, so `final_xor` will be the XOR of all values in `nums2`.
                - If both `nums1` and `nums2` have odd lengths, `final_xor` will be the result of XORing all values from `nums1` and `nums2`.
            3. Return `final_xor`.
        """

        final_xor = 0
        
        if len(nums1) % 2 == 0:
            # 如果 nums1 與 nums2 的長度都是偶數，則 XOR 結果為 0
            if len(nums2) % 2 == 0: 
                final_xor = 0
            # 如果 nums1 的長度是偶數，nums2 的長度是奇數，則只要計算 nums1 中的數值的 XOR 即可
            else:
                for n1 in nums1:
                    final_xor = final_xor ^ n1
        else:
            # 如果 nums2 的長度是偶數，nums1 的長度是奇數，則只要計算 nums2 中的數值的 XOR 即可
            if len(nums2) % 2 == 0:
                for n2 in nums2:
                    final_xor = final_xor ^ n2
            # 如果 nums1 與 nums2 的長度都是奇數，則 XOR 結果為 nums1 與 nums2 中所有數值的 XOR
            else:
                for n in (nums1 + nums2):
                    final_xor = final_xor ^ n

        return final_xor
