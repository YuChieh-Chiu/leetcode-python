class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        thought:
        - integer less than 0 would never be `palindrome`
        - integer equals to 0 is a `palindrome`
        - integer bigger than 0 should be check as below
            - reverse `x` by do the steps:
                (1) set the reverse to 0
                (2) get the last digit
                (3) update the reverse with reverse*10 + last digit
                (4) update `x` with `//=` to delete the last digit
                (5) repeat (1)~(4) till `x` = 0
            - if the reverse = `x`, then return True, else return False
        """
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            original = x
            reverse = 0
            while x != 0: 
                reverse = (reverse*10) + (x%10)
                x //= 10
            if reverse == original:
                return True
            else:
                return False
