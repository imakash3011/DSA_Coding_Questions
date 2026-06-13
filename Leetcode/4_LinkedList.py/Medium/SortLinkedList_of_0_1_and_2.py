'''https://takeuforward.org/plus/dsa/problems/sort-a-ll-of-0's-1's-and-2's?source=strivers-a2z-dsa-track'''



# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def sortList(self, head):

        lst = []
        temp = head

        while temp:
            lst.append(temp.data)
            temp = temp.next
        
        lst.sort()
        temp = head
        idx = 0
        while temp:
            temp.data = lst[idx]
            idx+=1
            temp = temp.next

        return head