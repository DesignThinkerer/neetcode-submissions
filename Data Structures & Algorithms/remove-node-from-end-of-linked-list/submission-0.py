# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Initialize dummy node and pointers
        dummy = ListNode(0, head)
        slow = fast = dummy
        
        # 2. Advance 'fast' n + 1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
            
        # 3. Move fast and slow until 'fast' hits the end
        while fast:
            fast, slow = fast.next, slow.next
            
        # 4. Skip the target node to remove it
        slow.next = slow.next.next
        
        # 5. Return the start of the list
        return dummy.next