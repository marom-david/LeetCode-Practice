class Solution(object):
    def groupAnagrams(self, strs):
        res = {}

        for word in strs:
            key = "".join(sorted(word))
            if key in res:
                res[key].append(word)
            else:
                res[key] = [word]

        return list(res.values())