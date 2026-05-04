# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if(head == None):
            return False
        if(head.next == None):
            return True
        stack = []
        slow,fast,current = head,head,head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        mid = slow
        while(mid != None):
            stack.append(mid.val)
            mid = mid.next
        while(len(stack)>0):
            if(stack.pop() != current.val):
                return False
            current = current.next
        return True 


        
        