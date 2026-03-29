# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        curr = head
        node_set = set()
        while curr:
            if curr in node_set:
                return True
            else:
                node_set.add(curr)
            curr = curr.next 
            
        return False

    