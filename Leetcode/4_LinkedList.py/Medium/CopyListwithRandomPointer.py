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
        if not head:
            return None
        
        old_to_new = {}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head

        while curr:
            old_to_new[curr].next = old_to_new.get(curr.val)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next
        
        return old_to_new[head]
    





class Solution:
    def copyRandomList(self, head):

        # Edge case:
        # If the original list is empty, there is nothing to copy.
        if not head:
            return None

        # Dictionary that stores:
        #
        # Original Node  ->  Copied Node
        #
        # Example:
        # old_to_new[original_A] = copy_A
        # old_to_new[original_B] = copy_B
        #
        # This mapping helps us quickly find the copied version
        # of any original node while setting next/random pointers.
        old_to_new = {}

        # -----------------------------------------------------
        # PASS 1:
        # Create a copy of every node.
        #
        # At this stage we ONLY create nodes.
        # We do NOT connect next or random pointers yet.
        # -----------------------------------------------------
        curr = head

        while curr:

            # Create a new node with the same value.
            copy_node = Node(curr.val)

            # Store relationship:
            # Original Node -> Copied Node
            old_to_new[curr] = copy_node

            # Move to next original node.
            curr = curr.next

        # -----------------------------------------------------
        # PASS 2:
        # Connect next and random pointers for copied nodes.
        #
        # Since every copied node already exists in our hashmap,
        # we can easily find:
        #
        # copied_next   = old_to_new[curr.next]
        # copied_random = old_to_new[curr.random]
        # -----------------------------------------------------
        curr = head

        while curr:

            # Get copied version of current node.
            copy_node = old_to_new[curr]

            # ---------------------------
            # Connect NEXT pointer
            # ---------------------------
            #
            # Original:
            # curr --------> curr.next
            #
            # Copy:
            # copy_node ---> copied version of curr.next
            #
            # Using .get() handles the case where
            # curr.next is None (last node).
            copy_node.next = old_to_new.get(curr.next)

            # ---------------------------
            # Connect RANDOM pointer
            # ---------------------------
            #
            # Original:
            # curr.random ---> some node
            #
            # Copy:
            # copy_node.random ---> copied version
            #                        of that node
            #
            # Using .get() also handles:
            # curr.random = None
            copy_node.random = old_to_new.get(curr.random)

            # Move to next original node.
            curr = curr.next

        # Return copied version of original head.
        return old_to_new[head]