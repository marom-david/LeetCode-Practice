class Solution(object):

    def __init__(self, nums):
        self.original = list(nums)
        self.array = nums
        

    def reset(self):
        self.array = list(self.original)
        return self.array
        

    def shuffle(self):
        arr = self.array
        n = len(arr)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            arr[i], arr[j] = arr[j], arr[i]

        return self.array
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()