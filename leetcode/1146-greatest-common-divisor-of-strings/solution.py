class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # go through each beginmning , find longest pre that also divides both
        if (str1+str2!=str2+str1):
            return ""
        max_len = gcd(len(str1), len(str2))
        return str1[:max_len]
            
