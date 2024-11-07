# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        thought:
        - From the problem description, we know:
            - Two non-empty linked lists represent two non-negative integers.
            - There will be no leading zeros.
        - Our goal is to add these two non-negative integers and output the result as a new linked list.
        - Steps:
            (1) First, initialize an empty linked list `lm` and set `current` to point to `lm`, allowing us to create each node of the new linked list as we go. Initialize `prev_digit2` to track the carry-over value.
            (2) In a while loop, traverse both linked lists node by node, adding values from corresponding positions.
                - If the sum is greater than 9, remember to carry over the tens place value to the next position.
            (3) Continue adding the sum of values to the empty linked list until all nodes have been processed.
                - After the loop ends, check one final time for any remaining carry-over.
                - The result should return as `lm.next` since lm is the initial empty node.
        """
        lm = ListNode()
        current = lm
        prev_digit2 = 0
        while (l1 is not None) or (l2 is not None):
            if l1 is None:
                tot = l2.val + prev_digit2
                l2 = l2.next
            elif l2 is None:
                tot = l1.val + prev_digit2
                l1 = l1.next
            else:
                tot = l1.val + l2.val + prev_digit2
                l1 = l1.next
                l2 = l2.next
            current.next = ListNode(tot % 10)
            prev_digit2 = tot // 10
            current = current.next 
        if prev_digit2 > 0:
            current.next = ListNode(prev_digit2)
        return lm.next
