class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLL:

    def __init__(self):
        self.head = None

    # 1. Insert at head
    def insert_at_head(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
    

    def insert_at(self, val, position):
        new_node = Node(val)
        if position ==0:
            self.insert_at_head(val)
            return
        
        current = self.head
        count = 0
        while current and count < position -1:
            current = current.next
            count+=1
        
        if current is None:
            print("Position out of bounds")
            return
        
        new_node.next = current.next
        new_node.prev = current
        if current.next:  ## to check if current is last node or not

            current.next.prev = new_node
        current.next = new_node
    
    def traversal_forward(self):
        if self.head is None:
            print("Empty!")
            return
        current = self.head
        while current is not None:
            print(current.val, end=" ")
            current = current.next
        print()

    def traversal_backward(self):
        if self.head is None:
            print("Empty!")
            return
        # 1. Walk forward to find the very last node
        current = self.head
        while current.next is not None: # Stop AT the last node, not after it
            current = current.next
        # 2. Walk backward from the last node to the head
        while current is not None:  # Process every node until we run out
            print(current.val, end=" ") # Using end=" " keeps it on one line
            current= current.prev
        print()

    def reverse_doubly_ll(self):
        # Edge case: Empty list or only one node present
        if self.head is None or self.head.next is None:
            return self.head
        
        current = self.head
        prev_node = None  # self.head.prev is already None, but setting it explicitly is cleaner

        while current is not None:
            # Track the next node before we overwrite pointers
            front = current.next
            
            # Flip the pointers
            current.next = prev_node
            current.prev = front    
            
            # Move our placeholders forward
            prev_node = current
            current = front
            
        # Update the actual head of the list object
        self.head = prev_node
        return self.head
    
    
    def delete_all_occur_key(self, key):
        # Edge case: Empty list
        if self.head is None:
            return self.head
        
        curr = self.head

        while curr is not None:  # Go all the way to the end node
            if curr.val == key:
                # Save the next node before we disconnect curr
                next_node = curr.next 
                
                # Case 1: Deleting the head node
                if curr == self.head:
                    self.head = next_node
                    if self.head is not None:
                        self.head.prev = None
                
                # Case 2: Deleting a middle or tail node
                else:
                    curr.prev.next = curr.next
                    if curr.next is not None:  # If it's not the tail node
                        curr.next.prev = curr.prev
                        
                # Move to the next node (curr is now disconnected)
                curr = next_node
            else:
                # Only move forward normally if we DIDN'T delete anything
                curr = curr.next
                
        return self.head


        

    

dll= DoublyLL()
dll.traversal_forward()

# Test 1: Insert at head
print("Testing insert_at_head (Adding 10, then 20):")
dll.insert_at_head(10)
dll.insert_at_head(20)
dll.traversal_forward()
dll.traversal_backward()


# Test 2: Append
print("Testing append (Appending 30, then 40):")
dll.append(30)
dll.append(20)
dll.traversal_forward()  # Expected: 20 <-> 10 <-> 30 <-> 40
dll.traversal_backward()


# Test 3: Insert at position 0 (should use insert_at_head logic)
print("Testing insert_at position 0 (Inserting 99):")
dll.insert_at(99, 0)
dll.traversal_forward()  # Expected: 99 <-> 20 <-> 10 <-> 30 <-> 40
# dll.traversal_backward()


# Test 4: Out of bounds error handling
# print("Testing insert_at out of bounds (position 20):")
# dll.insert_at(100, 20)  # Expected: Prints "Position out of bounds"

# dll.reverse_doubly_ll()
# dll.traversal_forward()

dll.delete_all_occur_key(20)
dll.traversal_forward()