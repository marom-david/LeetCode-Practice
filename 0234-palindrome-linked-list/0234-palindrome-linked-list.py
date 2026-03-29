# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if not head:
            return True
            
        curr = head
        currRe = self.reverse(self.middle(head))

        while currRe:
            if currRe.val != curr.val:
                return False
            currRe = currRe.next
            curr = curr.next
                
        return True
    
    def middle(self, head):
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next
            fast = fast.next
            slow = slow.next

        return slow

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next 
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev