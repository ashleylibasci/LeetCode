class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        res = []
        max = candies[0]
        for i in candies:
            if (i > max):
                max = i
        for j in candies:
                if (j+extraCandies >= max):
                    res.append(True)
                else:
                    res.append(False)
        return res