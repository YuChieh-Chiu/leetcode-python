# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        thought:
        - the problem description states that the linked list is sorted in ascending order.
        - our goal is to delete all duplicates so that each element appears only once, and the linked list remains sorted.
        - to achieve this, we should traverse the linked list element by element. If an element is the same as the next one, we delete the next element.
            - We delete the next element because it is easier to implement.
        - the steps to follow are:
            (1) traverse the linked list until the next pointer is `None`, indicating the end of the list.
            (2) for each element, check if its value is the same as the value of the next element:
                - if they are the same, update the current element's next pointer to skip the next element.
                - if they are different, move to the next element.
            (3) return the modified linked list.
        """
        current = head
        while current:
            nextNode = current.next
            if nextNode:
                if current.val == nextNode.val:
                    current.next = nextNode.next
                else:
                    current = current.next
            else:
                return head
        return head
