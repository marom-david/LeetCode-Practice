# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        dummy = ListNode(0, head)
        mid = self.middle(head)
        sec = mid.next
        mid.next = None
        currRe = self.reverse(sec)
        curr = head

        while currRe:
            temp1 = curr.next
            temp2 = currRe.next

            curr.next = currRe
            currRe.next = temp1

            curr = temp1
            currRe = temp2
        
        return dummy.next

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
        
    def middle(self, head):
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next
            fast = fast.next
            slow = slow.next

        return slow