class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0] * 26
        window = [0] * 26

        if len(s1) > len(s2): return False 

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        match = 0
        for i in range(26): 
            if s1_count[i] == window[i]:
                match += 1
        
        l = 0 

        for r in range(len(s1), len(s2)):
            if match == 26: 
                return True 
            
            #add s2[r]
            index = ord(s2[r]) - ord('a')
            window[index] += 1 

            if window[index] == s1_count[index]:
                match += 1 
            elif window[index] == s1_count[index] + 1:
                match -= 1

            #remove s2[l]
            index = ord(s2[l]) - ord('a')
            window[index] -= 1

            if window[index] == s1_count[index]:
                match += 1 
            elif window[index] == s1_count[index] - 1:
                match -= 1
            
            l += 1 

        return match == 26
