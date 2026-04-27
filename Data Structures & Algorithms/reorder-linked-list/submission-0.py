# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the second half of the list
        first_half = head
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next

        # Split the list
        slow.next = None

        # Reverse the second half
        tail = None
        while second_half:
            tail,second_half.next,second_half = second_half, tail, second_half.next

        second_half = tail

        # merge

        while second_half:
            temp1 = first_half.next 
            temp2 = second_half.next
            
            first_half.next = second_half
            second_half.next = temp1

            first_half = temp1
            second_half = temp2

        return None