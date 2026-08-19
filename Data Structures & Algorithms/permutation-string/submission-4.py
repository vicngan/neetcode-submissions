from collections import Counter 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1 > n2: return False

        s1_count = Counter(s1) 
        window = Counter(s2[:n1]) #slices s2 from index -> n1; not including n1
        
        if s1_count == window: return True 

        #slide window across s2 
        for i in range (n1, n2): #i = index of a new character entering the window 
            #add character entering window
            window[s2[i]] += 1 #count in window for character at position i in s2
            
            #remove char leaving the window 
            l_char = s2[i - n1] #index of the character before the window begin in s2
            window[l_char] -= 1

            #remove a char key from the counter once it's = 0
            if window[l_char] == 0: 
                del window[l_char]

            if window == s1_count:
                return True 
        
        return False 


