class Solution(object):
    def lemonadeChange(self, bills):
        five = 0
        ten = 0
                        
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else: return False
            elif b == 20:
                if ten > 0:
                    ten -= 1
                    if five > 0:
                        five -=1
                    else: return False
                elif five > 2:
                    five -= 3
                else: return False
            
            
        return True