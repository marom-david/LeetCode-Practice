class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        x_arr = []
        x_itr = x
        j = 0
        while x_itr > 0:
            x_arr.append(x_itr%10)
            x_itr = x_itr//10

        x_reverse = x_arr[::-1]
        i = 0
        while i < len(x_arr) and x_arr[i] == x_reverse[i]:
            i = i + 1
        
        if i == len(x_arr):
            return True

        return False
        