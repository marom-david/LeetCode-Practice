class Solution(object):
    def romanToInt(self, s):       
        dict = {'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
            }

        sum = 0
        c = 0
        while c != len(s):
            if c + 1 < len(s) and dict[s[c]] < dict[s[c + 1]]:
                sum = sum - dict[s[c]]
            else:
                sum = sum + dict[s[c]]
            c = c + 1

        return sum