# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = ListNode()
        node.next = head
        point = node
        while(point.next != None):
            if(point.next.val == val):
                point.next = point.next.next
            else:
                point = point.next
        return node.next
        