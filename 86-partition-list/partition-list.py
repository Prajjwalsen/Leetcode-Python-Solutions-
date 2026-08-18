# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smalldummy = ListNode(0)
        largedummy = ListNode(0)

        small = smalldummy
        large = largedummy

        current = head

        while current:
            
            if current.val < x:
                small.next = current
                small = small.next

            else:
                large.next = current
                large = large.next

            current = current.next

        small.next = largedummy.next
        large.next = None

        return smalldummy.next
        