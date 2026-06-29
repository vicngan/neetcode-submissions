class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char = set(s) 
        res = 0

        for c in char: 
            maxFreq = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    maxFreq += 1 
                while (r - l + 1) - maxFreq > k:
                    if s[l] == c: 
                        maxFreq -= 1 
                    l += 1
                res = max(res, r - l + 1)
        return res