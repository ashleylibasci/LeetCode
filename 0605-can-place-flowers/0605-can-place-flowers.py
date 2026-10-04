class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        flowerLen = len(flowerbed)
        i = 0
        while i < flowerLen:
            if ((flowerbed[i] == 0) and ((i == 0) or (flowerbed[i-1] == 0)) and ((i == (flowerLen - 1)) or (flowerbed[i+1] == 0))):
                count+=1
                i+=2
            else:
                i+=1
        return count >= n