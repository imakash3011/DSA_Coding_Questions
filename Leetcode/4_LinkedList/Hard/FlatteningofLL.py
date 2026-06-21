# Definition of singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None, child=None):
#         self.val = val
#         self.next = next
#         self.child = child

class Solution:
    def flattenLinkedList(self, head):
        if not head:
            return None
            
        curr = head
        arr = []

        # --- STEP 1: Collect all elements into the array ---
        while curr:
            # Append the main node's value
            arr.append(curr.val)
            
            # If a child list exists, loop down and save its values
            if curr.child:
                child_curr = curr.child
                while child_curr:
                    arr.append(child_curr.val)
                    child_curr = child_curr.next  # Move down the child list
            
            # Move to the next horizontal node
            curr = curr.next

        # --- STEP 2: Sort the array ---
        # Using Python's built-in Timsort (which is a hybrid Merge Sort)
        arr.sort()

        # --- STEP 3: Rebuild the flattened list ---
        # Create a dummy node to easily construct the new list
        dummy = ListNode(-1)
        new_curr = dummy
        
        for value in arr:
            new_curr.next = ListNode(value)
            new_curr = new_curr.next
            
        return dummy.next