'''https://leetcode.com/problems/next-greater-node-in-linked-list/description/?envType=problem-list-v2&envId=linked-list'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
#         # 1. Convert linked list to a python list (Fixed your typo here)
#         lst = []
#         curr = head
#         while curr:
#             lst.append(curr.val)
#             curr = curr.next
        
#         final_result = []
        
#         # 2. Iterate through every element in the list
#         for i in range(len(lst)):
#             found_larger = False
            
#             # Look at every element AFTER the current one (lst[i+1:])
#             for j in range(i + 1, len(lst)):
#                 if lst[j] > lst[i]:
#                     final_result.append(lst[j])
#                     found_larger = True
#                     break # We found the NEXT larger, so stop looking!
            
#             # If we reached the end and didn't find anything larger
#             if not found_larger:
#                 final_result.append(0)
                
#         return final_result
            


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        curr = head
        lst = []
        while curr:
            lst.append(curr.val)
            curr = curr.next
        
        final_lst = [0]*len(lst)
        stack = []
        for i in range(len(lst)):
            while stack and lst[stack[-1]]<lst[i]: # taking out corresopnding value of that index
                prev_index = stack.pop() 
                final_lst[prev_index] = lst[i]  
            stack.append(i)  ## appending index not actual value
        
        return final_lst

