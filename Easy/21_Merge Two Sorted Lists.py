# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        thought:
        - from the problem description, we know that `list1` and `list2` are both in non-descending order.
        - our goal is to merge two linked lists into one sorted linked list.
        - to achieve this, we can traverse through both lists, comparing elements one by one, and add the smaller element to a new linked list.
        - therefore, we can follow these steps:
            (1) if `list1` or `list2` is empty, return the non-empty list.
            (2) create an empty ListNode to represent the beginning of the new linked list.
            (3) traverse through `list1` and `list2`, comparing their elements:
                - insert the smaller element at the end of the new linked list.
            (4) if one list is fully traversed, append the remaining elements from the other list to the new linked list.
            (5) return the new linked list.
        """

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        merged = ListNode()
        current = merged
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return merged.next
