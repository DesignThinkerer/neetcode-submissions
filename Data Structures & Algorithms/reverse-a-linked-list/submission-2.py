# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        while head:
            # first we save what is the next item in the linked list
            next_node = head.next 
            # then we make the current list item look to the previous item instead of next_node
            head.next = tail
            # then we say that the previous node is actually the current node
            tail = head
            # and we end by saying that we want to continue the list
            head = next_node
            
    
        return tail