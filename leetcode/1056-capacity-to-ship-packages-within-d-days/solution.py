class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        def capacity(num)->bool:
            curr_days = 1
            curr_load=0
            for weight in weights:
                if (curr_load+weight>num):
                    curr_load = weight
                    curr_days +=1
                else:
                    curr_load+=weight
            return curr_days<=days
        while (left < right):
            mid = (left+right)//2
            if (capacity(mid)):
                right = mid
            else:
                left = mid+1
        return right

        
