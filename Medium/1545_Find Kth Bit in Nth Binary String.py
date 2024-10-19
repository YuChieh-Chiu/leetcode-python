class Solution:
    def recursion(self, previous: str) -> str:
        previous_ri = previous.replace('0', '2').\
                            replace('1', '0').\
                            replace('2', '1')
        previous_ri = previous_ri[::-1]
        return previous + "1" + previous_ri
    def findKthBit(self, n: int, k: int) -> str:
        """
        thought:
        - Our goal is to generate the binary string `Sn` and find the `Kth` value in it.
        - From the problem description, we understand the definition of `Si` as follows:
            - S1 = '0'
            - Si = Si-1 + '1' + reverse(invert(Si-1)) for i > 1
        - We can break down this definition into the following steps:
            1. Initialize `S` as '0'.
            2. Define a recursive function to calculate `Si`. The function will:
                - First, invert the characters in the string (i.e., change all '0's to '1's and all '1's to '0's).
                - Second, reverse the string.
                - Finally, concatenate the original string, '1', and the reversed-inverted string.
            3. After generating the binary string `Sn`, use indexing to find the `Kth` value.
                - Note that `K` starts from 1, while the string index starts from 0.
        """
        s = '0'
        for i in range(1, n):
            s = self.recursion(s)
        return s[k-1]
