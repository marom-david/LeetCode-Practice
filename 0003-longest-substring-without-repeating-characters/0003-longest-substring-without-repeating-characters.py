class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        max_sub = 0
        char_set = set()
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            if right - left + 1 > max_sub:
                max_sub = right - left + 1

        return max_sub



        