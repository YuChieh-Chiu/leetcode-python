class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        thought:
        - From the problem description, we can identify the following information and constraints:
            - The `divisor` is not zero.
            - The result of dividing `dividend` by `divisor` should be an integer.
            - The use of multiplication, division, and power operators is prohibited.
            - Only 32-bit signed integers can be used.
        - Given these operator restrictions and the bit-width limitation, the solution will use `bit manipulation`.
        - Steps:
            (Hints by LLM)
            1. Use XOR to determine the sign of the result.
            2. Convert both `dividend` and `divisor` to their absolute values for easier computation.
            3. Perform a left bit-shift on `divisor` repeatedly (equivalent to multiplying by 2 each time) until `divisor` exceeds `dividend`. This helps "quickly" approximate the maximum bit length of the quotient. For example, if we find the maximum bit length of the quotient is 5, the binary representation of the quotient should be in the form `xxxxx`, where each `x` can be either 1 or 0.
            4. Starting from the leftmost bit (most significant bit), determine the value of each bit. For each bit position, if the current `dividend` is greater than or equal to the shifted `divisor`, set the bit to 1 since it contributes to the quotient. This bit corresponds to `2` raised to the current bit position in decimal form. Otherwise, set the bit to 0.
            5. Handle edge cases: if the resulting quotient is outside the range (-2)**31 to 2**31 - 1, return the closest boundary value.
        """
        # 1. Use XOR to determine the sign of the result.
        if dividend ^ divisor < 0:
            sign = -1
        else:
            sign = 1
        # 2. Convert both `dividend` and `divisor` to their absolute values for easier computation.
        dividend = abs(dividend)
        divisor = abs(divisor)
        # 3. Perform a left bit-shift on `divisor` repeatedly (equivalent to multiplying by 2 each time) until `divisor` exceeds `dividend`. This helps "quickly" approximate the maximum bit length of the quotient. For example, if we find the maximum bit length of the quotient is 5, the binary representation of the quotient should be in the form `xxxxx`, where each `x` can be either 1 or 0.
        pow2 = 0
        while dividend >= divisor:
            divisor = divisor << 1
            pow2 += 1
        divisor = divisor >> 1
        pow2 -= 1
        # 4. Starting from the leftmost bit (most significant bit), determine the value of each bit. For each bit position, if the current `dividend` is greater than or equal to the shifted `divisor`, set the bit to 1 since it contributes to the quotient. This bit corresponds to `2` raised to the current bit position in decimal form. Otherwise, set the bit to 0.
        quotient = 0
        while pow2 >= 0:
            if dividend >= divisor:
                quotient += 2**pow2
                dividend -= divisor
            divisor = divisor >> 1
            pow2 -= 1
        # 5. Handle edge cases: if the resulting quotient is outside the range (-2)**31 to 2**31 - 1, return the closest boundary value.
        if sign * quotient > (2**31 - 1):
            return 2**31 - 1
        elif sign * quotient < ((-2)**31):
            return (-2)**31
        else:
            return sign * quotient
