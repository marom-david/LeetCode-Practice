# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        remainder = 0
        dummy = ListNode()
        tail = dummy

        while l1 or l2:
            v1 = 0
            v2 = 0

            if l1 != None:
                v1 = l1.val
            if l2 != None:
                v2 = l2.val

            val = v1 + v2 + remainder
            tail.next = ListNode(val%10)
            tail = tail.next
            remainder = val//10
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if remainder: 
            tail.next = ListNode(remainder)
            tail = tail.next
        return dummy.next