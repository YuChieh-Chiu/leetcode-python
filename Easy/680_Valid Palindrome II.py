class Solution:
   def isPalindrome(self, s: str, left: int, right: int) -> bool:
       is_palindrome = True
       while left < right:
           if s[left] == s[right]:
               left += 1
               right -= 1
           else:
               is_palindrome = False
               break
       return is_palindrome
               
   def validPalindrome(self, s: str) -> bool:
       """
       Thought:
       - Goal: Determine if the string `s` can be palindrome or not after deleting **at most one** character from it.
       - Idea:
           1. Use two pointers approach to check palindrome: set one pointer at leftmost and another at rightmost, move both pointers toward center simultaneously.
           2. When characters don't match, we have exactly one deletion chance. At this point, we can either:
              - Delete the left character (move left pointer forward)
              - Delete the right character (move right pointer backward)
           3. Try **both possibilities** and see if either results in a valid palindrome for the remaining substring.
       - Steps:
           1. Initialize two pointers: `left` at 0 and `right` at len(s)-1
           2. While left < right:
               - If s[left] == s[right]: move both pointers toward center
               - If s[left] != s[right]: this is our one mismatch
                 - Try skipping left character: check if s[left+1:right] is palindrome
                 - Try skipping right character: check if s[left:right-1] is palindrome
                 - If either option works, return True; otherwise return False
           3. If we complete the loop without mismatches, return True (already a palindrome)
       - Key Points:
           1. When we have only one deletion chance, we don't need to track deletion count because after one deletion attempt, the result is binary (palindrome or not).
           2. When characters mismatch, we must try BOTH possibilities (skip left OR skip right) simultaneously rather than assuming left has priority, because either deletion could lead to a valid palindrome.
       """
       left = 0
       right = len(s)-1

       while left < right:
           if s[left] == s[right]:
               left += 1
               right -= 1
           else:
               if self.isPalindrome(s, left+1, right) or self.isPalindrome(s, left, right-1):
                   return True
               else:
                   return False             

       return True
