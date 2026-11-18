class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        res = []
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num]+=1
        print(count)
        while k > 0:
            curr_max = max(count, key=count.get)
            res.append(curr_max)
            count.pop(curr_max)
            k-=1
        return res
