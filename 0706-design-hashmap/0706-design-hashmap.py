class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap(object):

    def __init__(self):
        self.size = 10007
        self.table = [ListNode() for _ in range(self.size)]

    def _hash(self, key):
        return key%self.size

    def put(self, key, value):
        idx = self._hash(key)
        curr = self.table[idx]

        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next

        curr.next = ListNode(key, value)
        

    def get(self, key):
        idx = self._hash(key)
        curr = self.table[idx]

        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        
        return -1

    def remove(self, key):
        idx = self._hash(key)
        curr = self.table[idx]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)