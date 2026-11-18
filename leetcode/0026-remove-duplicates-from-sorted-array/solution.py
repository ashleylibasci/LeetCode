class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        seen = set()
        k = 0
        for i in range(len(nums)):
            if nums[i] in seen:
                nums[i] = 101
            else:
                seen.add(nums[i])
                k+=1
        nums.sort()
        return k   
