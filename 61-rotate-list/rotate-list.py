# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        length = 1
        pointer = head

        while pointer.next:
            pointer = pointer.next
            length += 1

        k = k % length

        if k == 0:
            return head
        
        pointer.next = head

        steps = length - k

        for _ in range(steps):
            pointer = pointer.next

        new_head = pointer.next
        pointer.next = None

        return new_head
        