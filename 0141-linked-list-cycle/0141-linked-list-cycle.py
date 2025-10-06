# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Determines if a linked list has a cycle using the Tortoise and Hare algorithm.
        """
        if not head or not head.next:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next  # Moves one step
            fast = fast.next.next  # Moves two steps

            # If they meet, a cycle exists
            if slow == fast:
                return True

        # If the loop finishes, fast reached the end, so no cycle
        return False
