class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        final = ""
        c = 0
        while c < len(strs[0]):
            if all(s[c] == strs[0][c] for s in strs):
                final = final + strs[0][c]
            else:
                break
            c = c + 1
        
        return final
        