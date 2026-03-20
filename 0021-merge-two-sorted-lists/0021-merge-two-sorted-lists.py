# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        curr1 = list1
        curr2 = list2
        merged = ListNode()
        head = merged

        if not curr1:
            return curr2
        if not curr2:
            return curr1

        while curr1 and curr2:
            if curr1.val < curr2.val:
                head.next = curr1
                curr1 = curr1.next
            else:
                head.next = curr2
                curr2 = curr2.next
            head = head.next

            if curr1:
                head.next = curr1
            if curr2:
                head.next = curr2
            
        return merged.next