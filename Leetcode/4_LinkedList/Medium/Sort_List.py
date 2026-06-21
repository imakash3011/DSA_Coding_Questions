'''https://leetcode.com/problems/sort-list/description/'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## Use Merge sort for optimal solution

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        temp = head
        while temp :
            lst.append(temp.val)
            temp = temp.next
        
        lst.sort()
        print(lst)
        temp = head
        idx = 0
        while temp:
            temp.val = lst[idx]
            idx+=1
            temp = temp.next
        
        return head
        