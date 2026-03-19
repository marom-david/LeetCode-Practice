class Solution(object):
    def longestCommonPrefix(self, strs):
        min_len = float('inf')
        for str in strs:
            if len(str) < min_len:
                min_len = len(str)
        
        final = ""
        c = 0
        while c < min_len:
            if all(s[c] == strs[0][c] for s in strs):
                final = final + strs[0][c]
            else:
                break
            c = c + 1
        
        return final
        