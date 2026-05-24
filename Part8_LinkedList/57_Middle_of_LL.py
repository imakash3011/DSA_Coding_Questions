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


s1 = SinglyLL()
# print(s1.size_LL())

s1.append(10)
s1.append(20)
s1.append(30)
s1.append(40)
s1.traversal()

s1.insert_at(2, 87)
s1.traversal()

s1.delete(87)
s1.traversal()
# s1.append(50)
s1.traversal()
print(s1.middle_of_LL())


# node1 = Node(22)
# node2 = Node(33)
# node3 = Node(44)
# node4 = Node(55)

