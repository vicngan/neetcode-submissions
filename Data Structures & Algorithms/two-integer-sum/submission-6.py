class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for index, value in enumerate(nums): 
            diff = target - value
            if diff in hashMap:
                return [hashMap[diff], index]
            if diff not in hashMap:
                hashMap[value] = index 

