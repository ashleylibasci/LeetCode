import math
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        left = 1
        for i in range(len(nums)):
            res[i] = left
            print("res[i]: ", res[i])
            left *= nums[i]
            print("left: ", left)
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            print("res[i]: ", res[i])
            right *= nums[i]
            print("right: ", right)
        return res

