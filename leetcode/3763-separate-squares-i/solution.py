class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area= sum(l*l for x,y,l in squares)
        target = total_area/2.0
        left = min(y for x,y,l in squares)
        right = max(y+l for x,y,l in squares)
        def area(Y):
            total = 0
            for x,y,l in squares:
                height = max(0,min(Y-y,l))
                total+=height*l
            return total
        for i in range(60):
            mid = (left+right)/2
            if area(mid) < target:
                left=mid
            else:
                right=mid
        return right

