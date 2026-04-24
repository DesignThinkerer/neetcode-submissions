# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
        # 1. Create a dummy node to act as the starting anchor
        dummy = ListNode(0)
        current = dummy
        
        # 2. Only loop while BOTH lists have nodes to compare
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next  # Only move the pointer we used
            else:
                current.next = list2
                list2 = list2.next  # Only move the pointer we used
            
            current = current.next  # Move the tail of our new list forward
            
        # 3. If one list is longer than the other, 
        # just point the end of our new list to the remaining nodes.
        current.next = list1 if list1 else list2

        return dummy.next