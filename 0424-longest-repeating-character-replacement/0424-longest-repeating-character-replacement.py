class Solution(object):
    def characterReplacement(self, s, k):
        l = 0
        max_len = 0
        max_f = 0
        count = {}

        for r in range(len(s)):
            char = s[r]
            count[char] = 1 + count.get(char, 0)
            if max_f < count[char]:
                max_f = count[char]
            if (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1
            if max_len < (r - l + 1):
                max_len = (r - l + 1)
        
        return max_len
        