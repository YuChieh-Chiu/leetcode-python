# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        """
        Thought:
        - Goal:  
            - Return the decimal value of the binary number represented by the linked list.
        - Constraints:  
            - The linked list is not empty.  
            - Each node's value is either 0 or 1, meaning the list forms a binary number.
        - Idea:  
            - The problem can be broken down into two parts:  
                1. Traverse the linked list and collect the binary digits.  
                2. Convert the binary string to a decimal integer.
        - Steps:  
            1. Initialize a string variable `binary` with `'0b'` to indicate it's a binary number.  
            2. Set `current` to `head` to begin traversing the list.  
            3. While `current` is not None:  
                - Append the current node's value to the `binary` string.  
                - Move to the next node by updating `current = current.next`.  
            4. Return `int(binary, 2)` to convert the binary string to its decimal equivalent.
        """
        binary = '0b'
        current = head

        while current is not None:
            binary += str(current.val)
            current = current.next

        return int(binary, 2)
