class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)): #most intuitive but least efficient, loop through all elements 
            for j in range(i + 1, len(nums)):
                if nums[i]== nums[j]:
                    return True
        return False #O(n^2)/ O(1)
            
    #num.sort()                            sort the array 
    #for i in range (1, len(nums)):        iterate the array start from index 1 (2nd element)
    #   if nums(i) == nums(i - 1):         compare to the left element (previous), if equal, return True
    #       return True
    #   return False #O(logn)/ O(1) or O(n)

    #use a hashset
    #seen = set()                   create a set
    #for num in nums:               iterate through each element in nums 
    #   if num in seen:             if num in that seen set, return True (duplicate)
    #       return True 
    #   seen.add(num)               if not, add that number to the set 
    #return false                   if loop finishes without deuplicates, return false