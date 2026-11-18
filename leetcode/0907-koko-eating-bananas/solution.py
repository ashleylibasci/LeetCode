class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        if piles is None:
            return 0
        if len(piles)==h:
            return max(piles)
        left = 1
        right = max(piles)
        while left < right:
            mid = (left+right)//2
            hours = sum((pile_size+mid-1)//mid for pile_size in piles)
            if hours <= h:
                right = mid
            else:
                left =mid+1
        return left

        
