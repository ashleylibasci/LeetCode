class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        used = {}
        for i in range(len(nums)): #i=0, 1, i =1, 2
            need = k-nums[i] #need = 4, need 3
            if (need in used) and used[need] > 0:
                operations +=1
                used[need] -=1
            elif nums[i] not in used: #is 1 in dict? no so add it
                used[nums[i]] = 1 #dict now {"1":1, "2":1}
            else:
                used[nums[i]] +=1

        return operations
        #1. 2. 3
        #used = {1:1, 2:0, 3: 1}
        #operations = 1
        
