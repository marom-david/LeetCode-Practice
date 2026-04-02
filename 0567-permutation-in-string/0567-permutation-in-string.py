class Solution(object):
    def checkInclusion(self, s1, s2):
        s1_hash = {}
        for c in s1:
            s1_hash[c] = s1_hash.get(c, 0) + 1
        
        l = 0
        s2_hash = {}
        for r in range(len(s2)):
            right_char = s2[r]
            s2_hash[right_char] = s2_hash.get(right_char, 0) + 1
            
            if (r - l + 1) > len(s1):
                left_char = s2[l]
                s2_hash[left_char] = s2_hash.get(left_char, 0) - 1
                l += 1

                if s2_hash[left_char] == 0: del s2_hash[left_char]
            
            if s1_hash == s2_hash: return True

        return False




        

        