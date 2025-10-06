# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       
    
    # Create a dummy node to handle edge cases like removing the head
    dummy = ListNode(0, head)
    
    # Initialize both pointers at the dummy node
    slow = dummy
    fast = dummy

    # 1. Move the fast pointer n steps ahead
    for _ in range(n):
        fast = fast.next

    # 2. Move both pointers until fast reaches the last node
    while fast.next:
        slow = slow.next
        fast = fast.next
    
    # 3. 'slow' is now at the node before the target. Bypass the target node.
    slow.next = slow.next.next
    
    # The dummy's next is the new head of the list
    return dummy.next