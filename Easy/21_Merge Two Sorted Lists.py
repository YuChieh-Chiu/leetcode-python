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
        - our goal is to merge two linked list into one SORTED linked list.
        - it means that we can traverse through two lists elementwise, check which element is smaller, and add the smaller element into a new linked list.
        - therefore, we can follow these steps:
            (1) if `list1` or `list2` is empty, we can return `list2` or `list1` instead directly.
            (2) create a empty ListNode representing the beginning of a new linked list
            (3) traverse through `list1` and `list2` elementwise
                - check which one is smaller
                - insert the smaller one at the end of the new linked list
            (4) if `list1` or `list2` is traversed to the end, check the element in the other linked list, and insert the element at the end of the new linked list
            (5) return the new linked list 
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
