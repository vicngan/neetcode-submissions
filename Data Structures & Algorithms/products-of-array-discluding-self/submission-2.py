class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

    #left
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]  

    #right
        suffix = 1
        for i in range (len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res


