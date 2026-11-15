class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        maxN = 0
        left = 0
        zeroCount = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                zeroCount+=1
            if zeroCount > k:
                if (nums[left] == 0):
                    zeroCount -=1
                left+=1
            if (i-left+1) > maxN:
                maxN = i - left +1
        return maxN
        
