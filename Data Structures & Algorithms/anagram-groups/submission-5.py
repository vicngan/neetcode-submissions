class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping char count to list of anagrams; create a dict where every missing key gets an empty list as default value  

        for s in strs: #iterate through strings 
            count = [0]*26

            for char in s: #iterate through all characters
                count[ord(char) - ord("a")]+= 1 #count the frequency of each char (ASCII char - ASCII "a") and add one to count of char if found 
            res[tuple(count)].append(s) #group all anagrams of a particular count to result and then append s to result; default count changed from list to tuple bc tuple are immutable 
        return list(res.values()) #return the values of result ONLY instead of result and keys