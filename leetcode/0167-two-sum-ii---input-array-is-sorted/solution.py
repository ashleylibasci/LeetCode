class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers)-1
        while numbers[left]+numbers[right] != target:
            curr_sum = numbers[left]+numbers[right]
            if curr_sum < target:
                left +=1
            else:
                right -=1
        return [left+1, right+1]
