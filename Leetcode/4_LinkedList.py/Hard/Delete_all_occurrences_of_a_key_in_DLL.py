'''https://takeuforward.org/plus/dsa/problems/delete-all-occurrences-of-a-key-in-dll?source=strivers-a2z-dsa-track'''


class Solution:
    def deleteAllOccurrences(self, head, target):
        curr = head

        while curr:
            next_node = curr.next
            if curr.val == target:
                if curr.prev is not None:
                    curr.prev.next = curr.next
                else:
                    head = curr.next

                if curr.next is not None:
                    curr.next.prev = curr.prev
            curr = next_node
        return head