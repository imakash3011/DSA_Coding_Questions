class Node:
    def __init__(self, val):
        self.val = val
        self.next  = None

class SinglyLL:
    def __init__(self):   ## if no node exist then head will be None
        self.head = None
    
    def append(self, val):
        new_node = Node(val)

        if self.head is None:  ## If current no node is present so first will become head
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next 
            curr_node.next = new_node

    def traversal(self):
        if self.head is None:
            return "SLL is empty!"
        
        curr = self.head 
        while curr is not None:
            print(curr.val, end=" ")
            curr = curr.next
        print()
    
    def size_LL(self):
        if self.head is None:
            return "SLL is empty!"
        
        curr = self.head 
        count=0
        while curr is not None:
            # print(curr.val, end=" ")
            curr = curr.next
            count+=1
        print()
        return count

    
    def insert_at(self, idx, val):
        new_node = Node(val)  ## before inserting create a new node
        if idx == 0:
            new_node.next = self.head  ## connecting current node with past head node
            self.head = new_node ## making 0 index node as head 
        else:
            prev_node = None
            curr_node = self.head
            count = 0
            while curr_node is not None and count<idx:
                prev_node = curr_node
                curr_node = curr_node.next
                count+=1
            prev_node.next = new_node
            new_node.next = curr_node
    
    def get_val_of_index(self, idx):
        if idx==0:
            return self.head.val
        else:
            i=1
            curr = self.head
            while i<=idx:
                curr = curr.next
                i+=1
        return curr.val
        
    def delete(self, val):
        temp = self.head   ## representing the current node
        if temp.next is not None:
            if temp.val == val: ## if val is matching with head-value
                self.head = temp.next ## make next node as head
                return
            else:
                found = False  ## this helps to track whether node value is present or not. So that at the end we can print for value not present case
                prev = None
                while temp is not None:
                    if temp.val == val:  ## if you found the node where we have to make changes
                        found = True
                        break
                    prev = temp   ## see the following line as well
                    temp = temp.next
                if found:
                    prev.next = temp.next
                    return
                else:
                    print("Node not found!!")

    def Reverse_LL(self):
        prev = None
        temp = self.head
        
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

    ## This is the Brutforce Approach 
    # def middle_of_LL(self):
    #     n = self.size_LL()
    #     idx = n//2
    #     val = self.get_val_of_index(idx)        
    #     return val

    ## Optimal Use: Tortoise & Hare Approach (slow and fast pointer)
    def middle_of_LL(self):
        slow = self.head
        fast = self.head

        ## Order matters here... firstly fast and then fast.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.val
    
    ## Not optimised as per space (for time it will always take O(N))
    def  floyds_cycle(self):
        temp = self.head
        my_set = set()

        while temp is not None:
            if temp in my_set: 
                return True
            my_set.add(temp)
            temp = temp.next
        return False
    
    ## OPTIMISED SOLUTION as per Space (Two pointer - Tortoise and Hare Solution)
    def floyd_cycle_using_tortoise_hare(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def floyd_cycle_starting_point(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow.next.val
        return None
    
    def len_of_cycle_in_LL(self):
        slow = self.head
        fast = self.head

        # Step 1: Detect the cycle
        while fast is not None and fast.next is not None:
            slow= slow.next
            fast = fast.next.next

            if slow==fast:
                # Step 2: Cycle found, now count the length
                count = 1  # Start at 1 because we are going to move temp to the NEXT node
                temp = slow.next
                while temp is not slow:
                    count+=1
                    temp = temp.next
                return count
        return 0 # Return 0 if there is no cycle
        



# --- TESTING THE CYCLE DETECTION ---

# 1. Setup a fresh list
s_cycle = SinglyLL()
s_cycle.append(1)
s_cycle.append(2)
s_cycle.append(3)
s_cycle.append(4)
s_cycle.append(5)

# Current List: 1 -> 2 -> 3 -> 4 -> 5 -> None

# 2. Get references to the nodes we want to link
# Let's connect node '5' back to node '2'
head_node = s_cycle.head       # Node(1)
target_node = head_node.next   # Node(2)

# Find the last node (5)
last_node = head_node
while last_node.next is not None:
    last_node = last_node.next

# 3. Create the loop
last_node.next = target_node 

# 4. Check results
# WARNING: DO NOT call s_cycle.traversal() now, it will loop forever!
# print(f"Cycle detected (Starting Point): {s_cycle.floyd_cycle_starting_point()}")

print("Length of the cycle in Linked list: ",s_cycle.len_of_cycle_in_LL())
