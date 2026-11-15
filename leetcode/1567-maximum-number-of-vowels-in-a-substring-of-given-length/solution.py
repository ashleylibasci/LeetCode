class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        maxV = 0
        for i in range(0, len(s)-k+1): 
            substr = s[i:i+k] 
            sumV = sum(substr.count(v) for v in vowels)
            if (sumV > maxV):
                maxV = sumV
        return maxV
