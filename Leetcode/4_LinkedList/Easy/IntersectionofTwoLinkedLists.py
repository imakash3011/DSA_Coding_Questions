# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dct = {}
        temp = headA
        while temp:
            dct[temp] = dct.get(temp, 0)+1
            temp = temp.next
        
        temp = headB
        while temp:
            if temp in dct.keys():
                return temp
            temp = temp.next
        return None
        