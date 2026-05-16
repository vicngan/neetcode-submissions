class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_length = [0]*26
        t_length = [0]*26
        for i in range(len(s)):
            s_length [ord(s[i])-ord('a')] += 1 
            t_length [ord(t[i])-ord('a')] += 1 
        return True if s_length == t_length else False 
