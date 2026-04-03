class Solution(object):
    def asteroidCollision(self, asteroids):
        res = []
        
        for curr in asteroids:
            alive = True
            
            while res and res[-1] > 0 and curr < 0:
                if curr*(-1) < res[-1]:
                    alive = False
                    break
                if curr*(-1) == res[-1]:
                    alive = False
                    res.pop()
                    break
                if curr*(-1) > res[-1]:
                    res.pop()
            
            if alive:
                res.append(curr)
                              
        return res
        