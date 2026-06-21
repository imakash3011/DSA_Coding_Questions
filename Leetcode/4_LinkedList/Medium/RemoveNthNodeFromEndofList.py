'''https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Create a dummy node to handle edge cases (like removing the head)
        dummy = ListNode(0, head)
        
        # 2. Find the true length of the list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        # 3. Calculate steps needed from dummy to reach the node strictly BEFORE the target
        target_steps = length - n
        
        # 4. Traverse to the node right before the one we want to delete
        curr = dummy
        for _ in range(target_steps):
            curr = curr.next
            
        # 5. Delete the target node
        curr.next = curr.next.next
        
        # Return the real head (dummy.next), which safely handles if the original head was deleted
        return dummy.next

        