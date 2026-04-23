# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None

        while head:
            """
            head.next = tail: 
                The current node stops pointing forward and starts pointing backward
                to the new list we are building.
            
            tail = head: 
                We move our "reversed list" marker forward to include the current node.
            
            head = head.next: 
                We move the head to the original next node so we can continue the loop.
            """

            head.next, tail, head = tail, head, head.next

        return tail