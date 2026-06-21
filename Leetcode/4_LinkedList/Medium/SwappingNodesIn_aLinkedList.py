# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        n = 0
        lst = []
        while curr:
            lst.append(curr.val)
            cnt+=1
            curr = curr.next
        
        start = k-1
        end = n-k

        if start == end:
            return head
        
        lst[start], lst[end] = lst[end], lst[start]

        curr = head
        i=0
        while curr:
            curr.val = lst[i]
            i+=1
            curr = curr.next
        
        return head
    




class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Find the k-th node from the beginning
        left = head
        for _ in range(k - 1):
            left = left.next
            
        # Step 2: Find the k-th node from the end
        # 'fast' starts where 'left' is, 'right' starts at the head
        fast = left
        right = head
        
        while fast.next:
            fast = fast.next
            right = right.next
            
        # Step 3: Swap the values of the two nodes
        left.val, right.val = right.val, left.val
        
        return head