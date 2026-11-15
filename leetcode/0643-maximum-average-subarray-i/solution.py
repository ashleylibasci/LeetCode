class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max = sum(nums[0:k])/k
        substrSum = sum(nums[0:k])
        for i in range(1,len(nums)-k+1):
            #print("curr item: ", nums[i])
            substrSum = substrSum + nums[i+k-1]-nums[i-1]
            #print("substr: ", sub)
            avg = substrSum/k
            #print("curr avg: ", avg)
            #print("curr max: ", max)
            if (max < avg):
                max = avg
                #print("max updated")
        return max
