# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # first check if there is a root node
        if not root:
            return None
        # store in queue the root node
        queue = deque([root])
        # while the queue is not empty...
        while queue:
            # remove from the queue the current node
            node = queue.popleft() 
            # switch left and right nodes
            node.left, node.right = node.right, node.left
            # append the left and right node if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            # the loop will continue as long as the queue is not empty
            # it will be empty when the whole graph is traversed
        return root