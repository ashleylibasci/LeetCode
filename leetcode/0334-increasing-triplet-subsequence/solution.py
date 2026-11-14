class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        low = nums[0]
        second = float('inf')
        for num in nums:
            if (num <= low):
                low = num
            elif (num <= second):
                second = num
            else:
                return True
        return False
        
