'''https://leetcode.com/problems/palindrome-linked-list/description/'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr= curr.next
        # print(lst)
        if lst == lst[::-1]:
            return True
        return False
        