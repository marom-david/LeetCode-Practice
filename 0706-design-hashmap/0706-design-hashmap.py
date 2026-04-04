class MyHashMap(object):

    def __init__(self):
        self.hash_map = []

    def put(self, key, value):
        for i in range(len(self.hash_map)):
            if self.hash_map[i][0] == key:
                self.hash_map[i][1] = value
                return
        
        self.hash_map.append([key, value])
        

    def get(self, key):
        for the_key, value in self.hash_map:
            if the_key == key:
                return value
        return -1 
        

    def remove(self, key):
        for i in range(len(self.hash_map) - 1, -1, -1):
            if self.hash_map[i][0] == key:
                del self.hash_map[i]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)