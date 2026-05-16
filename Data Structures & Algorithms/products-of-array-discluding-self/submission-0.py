class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        pref =[0]*n
        suff = [0]*n

        pref[0] = 1
        suff[n-1] = 1 

        #prefix product array 
        for i in range(1,n): #for each i from 1 to n-1
            pref[i] = nums[i-1] * pref[i-1] #move forward
        #suffix product array
        for i in range(n-2, -1, -1): # for each i startingg from 2nd to last n to -1, backward step
            suff[i] = nums[i+1] * suff[i+1] #move backward
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res