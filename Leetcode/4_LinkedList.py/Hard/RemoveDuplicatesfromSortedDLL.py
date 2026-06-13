# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def removeDuplicates(self, head):
        if not head:
            return None

        curr = head

        while curr is not None and curr.next is not None:
            
            if curr.val == curr.next.val:
                next_node = curr.next
                curr.next = next_node.next

                if next_node.next is not None:
                    next_node.next.prev = curr
            else:
                curr = curr.next
        return head


