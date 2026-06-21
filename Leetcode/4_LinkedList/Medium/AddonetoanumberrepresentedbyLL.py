'''https://takeuforward.org/plus/dsa/problems/add-one-to-a-number-represented-by-ll?source=strivers-a2z-dsa-track'''



# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addOne(self, head):
        # Helper to reverse the linked list
        def reverse(node):
            prev = None
            curr = node
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        # 1. Reverse the list to make addition easier
        head = reverse(head)
        
        # 2. Add 1 and handle the carry
        curr = head
        carry = 1
        prev = None # We keep 'prev' so we know where the tail is if we need to add a new node
        
        while curr and carry:
            total = curr.val + carry
            curr.val = total % 10   # Store the digit (e.g., 10 becomes 0)
            carry = total // 10     # Calculate carry (e.g., 10 // 10 = 1)
            
            prev = curr
            curr = curr.next
            
        # If we finished the loop and still have a carry (e.g., 999 + 1 = 1000)
        # We need to append a new node at the end
        if carry:
            prev.next = ListNode(carry)
            
        # 3. Reverse the list back to its normal order
        return reverse(head)
