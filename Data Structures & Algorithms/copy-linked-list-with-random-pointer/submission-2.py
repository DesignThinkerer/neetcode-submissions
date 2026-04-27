"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         # Since the copy node might contain a reference to a random node
#         # that is yet to be created, we need to first create the nodes
#         # then go iterate trough the new list and set the random ref.

#         # We need an hashmap to map old nodes to their copy:
#         # We initialize the hashmap to {None : None} to prevents KeyError 
#         # when a node's next or random pointer is null, returning None naturally.
#         oldToCopy = { None : None } 

#         # first pass to clone the nodes
#         cur = head
#         while cur:
#             # copy the node
#             copy = Node(cur.val)
#             # map the copy to the node
#             oldToCopy[cur] = copy
#             # move cur to the next node to continue
#             cur = cur.next

#         # second pass to set the links
#         cur = head
#         while cur:
#             copy = oldToCopy[cur]
#             # now we can update the links
#             copy.next = oldToCopy[cur.next]
#             copy.random = oldToCopy[cur.random]
#             # move cur to the next node to continue
#             cur = cur.next

#         return oldToCopy[head]



# This can be done in O1 space, by mutating the list
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Step 1: Create new nodes and interweave them with original nodes
        # Original: A -> B -> C
        # Interleaved: A -> A' -> B -> B' -> C -> C'
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next
            
        # Step 2: Assign random pointers for the copy nodes
        # A'.random = A.random.next (which is the copy of A's random)
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        # Step 3: Separate the interleaved list back into two
        # Restore the original list and extract the copy list
        curr = head
        copy_head = head.next
        while curr:
            temp = curr.next
            curr.next = temp.next
            if temp.next:
                temp.next = temp.next.next
            curr = curr.next
            
        return copy_head