# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Thought:
        - Original Thought Process:
            - Given a ListNode, the objective is to remove the middle node (at the ⌊n/2⌋-th position).
            - The most straightforward approach is to traverse the entire linked list to determine its length `n`, and then perform a second pass to reach the `n//2`-th node. However, this requires two separate passes.
            - To achieve this in a single pass, we can use the two-pointer technique (fast and slow pointers), where one pointer travels at twice the speed of the other.
            - We also need to consider the edge case: if the list contains only a single node, we should handle it and return early.

        - Goal: Delete the middle node of a linked list and return its head.
        - Idea: Use the fast and slow pointers approach (Tortoise and Hare). To delete a node, we need to stop at the node immediately preceding it. By giving the fast pointer a "head start" (initializing it to head.next.next), the slow pointer will naturally land right before the middle node when the fast pointer reaches the end.
        - Steps:
            1. Handle the edge case: If the list has only one node, return None.
            2. Initialize `slow` to `head` and `fast` to `head.next.next`.
            3. Traverse the list: advance `slow` by 1 step and `fast` by 2 steps while `fast` and `fast.next` are valid.
            4. Remove the middle node by updating `slow.next` to `slow.next.next`.
            5. Return the modified `head`.
        - Time Complexity: O(n), where n is the number of nodes. We traverse the list at most once.
        - Space Complexity: O(1), as we only use two pointers regardless of the list size.
        """
        if not head.next:
            return None

        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return head
