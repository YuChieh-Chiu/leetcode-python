# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        """
        Thought:
        - Goal:
        Find the minimum and maximum distance between any two distinct critical points 
        (local maxima or local minima) in a singly-linked list. Return [-1, -1] if there 
        are fewer than two critical points.

        - Idea:
        Traverse the linked list once while tracking the previous value, current node, 
        and next node to identify critical points. Record the indices of the first 
        and most recent critical points. Update the minimum distance incrementally 
        as new critical points are found, and calculate the maximum distance at the end 
        using the difference between the last and first critical point indices.

        - Steps:
            1. Return [-1, -1] immediately if the linked list has fewer than 3 nodes.
            2. Initialize variables to track `first_idx`, `last_idx`, `min_distance`, `current_idx`, and `prev_val`.
            3. Iterate through the linked list node by node.
            4. For nodes with valid previous values and next neighbors, evaluate if the current node value is a local minimum or maximum.
            5. If a critical point is identified:
                - Record its index as `first_idx` if it is the first critical point encountered.
                - Otherwise, calculate the distance from `last_idx` and update `min_distance`.
                - Update `last_idx` to `current_idx`.
            6. Update `prev_val`, advance the `current` pointer, and increment `current_idx`.
            7. Compute `max_distance` as `last_idx - first_idx` if at least two critical points exist; otherwise, keep it as -1.
            8. Return `[min_distance, max_distance]`.

        - Time Complexity:
        O(N), where N is the number of nodes in the linked list, since we traverse the list only once.

        - Space Complexity:
        O(1), as we only use a constant amount of extra memory to store pointers and indices.
        """
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        first_idx = None
        last_idx = None
        min_distance = -1
        current = head
        current_idx = 0
        prev_val = None

        while current is not None:
            next_node = current.next

            if prev_val is not None and next_node is not None:
                is_local_min = (prev_val > current.val and next_node.val > current.val)
                is_local_max = (prev_val < current.val and next_node.val < current.val)
                
                if is_local_min or is_local_max:
                    if last_idx is not None:
                        distance = current_idx - last_idx
                        min_distance = distance if min_distance == -1 else min(min_distance, distance)
                    else:
                        first_idx = current_idx
                    last_idx = current_idx

            prev_val = current.val
            current = current.next
            current_idx += 1

        max_distance = (last_idx - first_idx) if (last_idx and first_idx and last_idx != first_idx) else -1

        return [min_distance, max_distance]
