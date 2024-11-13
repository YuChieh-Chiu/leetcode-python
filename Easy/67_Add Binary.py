class Solution:
    def binary2decimal(self, binary_string: str) -> int:
        decimal = 0
        power = len(binary_string)-1
        for char in binary_string:
            decimal += (2**power) * int(char)
            power -= 1
        return decimal
    def addBinary(self, a: str, b: str) -> str:
        """
        thought:
        - According to the problem description, `a` and `b` are binary strings with no leading zeros, except when `a` or `b` is simply '0'.
        - Our goal is to compute the binary string representation of `c`, which is the sum of `a` and `b` after converting them to decimal. This will involve basic bit manipulation.
        - Steps:
            (1) Define a function to convert a binary string to its decimal (integer) form.
            (2) Use this function to convert `a` and `b`, then add the two resulting decimal values.
            (3) Convert the sum back into a binary string and return it as the final result.
        """
        int_a = self.binary2decimal(a)
        int_b = self.binary2decimal(b)
        c = int_a + int_b
        
        power_c = 0
        while c >= 2**power_c:
            power_c += 1
        if power_c > 0:
            power_c -= 1
        binary_c = ""
        while power_c >= 0:
            if c >= 2**power_c:
                binary_c += "1"
                c -= 2**power_c
            else:
                binary_c += "0"
            power_c -= 1
        return binary_c
