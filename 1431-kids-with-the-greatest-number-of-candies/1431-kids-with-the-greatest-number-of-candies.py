class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
         n = len(candies)
         result = [False]*n
         max_can = max(candies)
         for i in range(n):
            if (candies[i] + extraCandies >= max_can):
                result[i] = True
         return result
