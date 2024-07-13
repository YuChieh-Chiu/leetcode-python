class Solution:
    def reverseParentheses(self, s: str) -> str:
        """
        thought:
        - IMPORTANT: the first encountered ")" is the right parenthesis of the innermost substring.
        - Therefore, we can follow these steps:
            (1) traverse the string from left to right. 
                - if the character is not ")", add it to the stack. 
                - if the character is ")", it indicates that we have found the first encountered ")", proceed to step (2).
            (2) to reverse the substring inside the parentheses, we can use the `stack` to achieve this with the LIFO (Last In, First Out) concept: while there are characters in the stack and the top of the stack is not "(", pop characters from the stack and append them to `temp` (reversing from right to left).
            (3) after the loop in step (2) ends, pop the last character from the stack (which corresponds to the "("), and add the reversed substring to the stack, preparing for the next reversal inside the next pair of parentheses.
            (4) repeat the above steps until the end. Finally, join the characters in the list to form the final string.
        """
        stack = []
        for char in s:
            if char == ")":
                temp = []
                while stack & stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()  # Remove "("
                stack.extend(temp)
            else:
                stack.append(char)
        return "".join(stack)
