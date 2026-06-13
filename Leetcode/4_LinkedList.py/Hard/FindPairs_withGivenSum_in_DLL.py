class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def findPairsWithGivenSum(self, head: Node, target: int) -> list[list[int]]:
        pairs = []
        if not head:
            return pairs
            
        # 1. Find the tail of the DLL
        left = head
        right = head
        while right.next is not None:
            right = right.next
            
        # 2. Two-pointer traversal
        # The boundary condition left.val < right.val ensures they do not cross
        while left is not None and right is not None and left.val < right.val:
            current_sum = left.val + right.val
            
            if current_sum == target:
                pairs.append([left.val, right.val])
                # Safely advance both pointers
                left = left.next
                right = right.prev
                
            elif current_sum < target:
                # We need a larger value, move left pointer forward
                left = left.next
                
            else:
                # We need a smaller value, move right pointer backward
                right = right.prev
                
        return pairs