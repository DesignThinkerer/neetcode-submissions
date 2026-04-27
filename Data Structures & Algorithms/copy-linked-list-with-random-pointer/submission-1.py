"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Since the copy node might contain a reference to a random node
        # that is yet to be created, we need to first create the nodes
        # then go iterate trough the new list and set the random ref.

        # We need an hashmap to map old nodes to their copy:
        # The hashmap is initialized to None because we might
        # get an old None node
        oldToCopy = { None : None } 

        # we iterate trough the entire list
        cur = head
        while cur:
            # first we create a deep copy of the node
            copy = Node(cur.val)
            # next we store the copy in our hashmap
            oldToCopy[cur] = copy
            cur = cur.next

        # second iteration, to set the random links
        cur = head
        while cur:
            copy = oldToCopy[cur]
            # now we update the next and random link
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]
