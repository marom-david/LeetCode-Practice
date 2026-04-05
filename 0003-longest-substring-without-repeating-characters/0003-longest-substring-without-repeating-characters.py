class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        counter = 0
        dic = {}

        for r in range(len(s)):
            dic[s[r]] = dic.get(s[r], 0) + 1
            if dic.get(s[r], 0) > 1:
                while dic[s[r]] != 1:
                    dic[s[l]] = dic.get(s[l], 0) - 1     
                    l +=1
            counter = max(counter, r-l+1)

        return counter