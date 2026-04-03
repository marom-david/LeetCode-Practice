class Solution(object):
    def findAnagrams(self, s, p):
        p_dict = {}
        for w in p:
            p_dict[w] = p_dict.get(w, 0) + 1

        res = []
        s_dict = {}
        l = 0
        counter = 0
        for r in range(len(s)):
            s_dict[s[r]] = s_dict.get(s[r], 0) + 1
            if s_dict == p_dict:
                res.append(l)
            if r - l + 1 >= len(p):
                s_dict[s[l]] = s_dict.get(s[l], 0) - 1
                if s_dict[s[l]] == 0:
                    del s_dict[s[l]]
                l += 1

        return res

        



        