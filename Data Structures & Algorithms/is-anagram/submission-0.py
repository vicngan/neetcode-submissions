class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sl = [0]*26
        tl = [0]*26
        for i in range(len(s)):
            sl[ord(s[i]) - ord('a')] += 1
            tl[ord(t[i]) - ord('a')] += 1
        return True if sl == tl else False
