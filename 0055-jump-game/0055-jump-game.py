class Solution(object):
    def canJump(self, nums):
        farest = 0

        for i, jump in enumerate(nums):
            if i > farest:
                return False
            farest = max(farest, i + jump)
        
        return True
            
        