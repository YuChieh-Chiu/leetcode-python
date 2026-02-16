class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Thought:
        - Goal: Reverse the bits of a given 32-bit signed integer and return the result as an integer.
        - Idea: Instead of converting to a string, use bitwise operations to directly manipulate the integer's binary representation, ensuring all 32 bits (including leading zeros) are processed.
        - Steps:
            1. Mask the input with 0xffffffff to handle Python's arbitrary-precision integers and treat the input as a 32-bit unsigned entity.
            2. Initialize 'res' to 0.
            3. Loop 32 times:
                a. Left shift 'res' by 1 to make space for the next bit.
                b. Extract the least significant bit (LSB) of 'n' using 'n & 1'.
                c. Place the extracted bit into the LSB of 'res' using the '|' operator.
                d. Right shift 'n' by 1 to prepare the next bit for extraction.
            4. Return the accumulated 'res'.
        - Time Complexity: O(1) - The loop always runs exactly 32 times regardless of the input value.
        - Space Complexity: O(1) - Only a constant amount of extra space is used for variables.
        """
        res = 0
        n &= 0xffffffff  # Ensure n is treated as a 32-bit unsigned integer
        
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
            
        return res
