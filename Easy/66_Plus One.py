class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Thought:
        - Goal:
            - Increment the given array of digits (representing a large integer) by one and return the resulting array.
        - Notes:
            - The array does not contain any leading zeros.
        - Steps:
            1. Initialize `carry` as True, representing the need to add 1 to the number.
            2. Iterate through `digits` from the last element to the first:
                - If `carry` is True, add 1 to the current digit.
                    - If the result equals 10, set the current digit to 0 and keep `carry` as True.
                - Otherwise, update the digit and set `carry` to False.
            3. If `carry` is still True after the loop, insert 1 at the beginning of the array.
        """

        carry = True

        for i in range(len(digits)-1, -1, -1):
            current = digits[i]
            if carry:
                current += 1
                if current == 10:
                    current = 0
                else:
                    carry = False
            digits[i] = current

        if carry:
            digits.insert(0, 1)

        return digits
