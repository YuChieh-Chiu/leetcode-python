class Solution:
    def intToRoman(self, num: int) -> str:
        """
        thought:
        - the problem gives us some constraints:
            (1) the symbols we can use are: I, V, X, L, C, D, M, IV, IX, XL, XC, CD, CM.
            (2) apart from the values corresponding to the symbols mentioned in (1), other values can only be obtained by subtracting symbols.
            (3) I, X, C, and M can be repeated up to three times, but if they need to be repeated a fourth time, they must be represented by adding symbols.
            (4) 1 <= `num` <= 3999
        - therefore, we can follow these steps:
            (1) first, define the symbols and their corresponding values.
            (2) split `num` into units, tens, hundreds, and thousands.
            (3) for each segment, use the corresponding symbols and values for computation:
                - leading num = 1~3: 1 * leading num
                - leading num = 4,5,9: directly convert the leading num
                - leading num = 6~8: 5 + (leading num - 5)
            (4) output the final result.
        """
        roman = ""
        s2v = [
            {1: "M"}, # 4 digits
            {1: "C", 4: "CD", 5: "D", 9: "CM"}, # 3 digits
            {1: "X", 4: "XL", 5: "L", 9: "XC"}, # 2 digits
            {1: "I", 4: "IV", 5: "V", 9: "IX"} # 1 digit
        ]
        num = "%04d" % num # let `num` to be 4 digits
        for i, n in enumerate(num):
            s2v_i = s2v[i]
            n = int(n)
            if n in [1,2,3]:
                roman_i = s2v_i[1]*n
            elif n in [4,5,9]:
                roman_i = s2v_i[n]
            elif n in [6,7,8]:
                roman_i = s2v_i[5] + s2v_i[1]*(n%5)
            else: # n=0
                roman_i = ""
            roman += roman_i
        return roman
