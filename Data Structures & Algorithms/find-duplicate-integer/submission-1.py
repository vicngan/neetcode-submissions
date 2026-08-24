class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]] #2 ptr jumps array

        while slow != fast: #stop once slow == fast 
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow_2 = 0 

        while slow != slow_2: 
            slow, slow_2 = nums[slow], nums[slow_2]
        
        return slow 




        


