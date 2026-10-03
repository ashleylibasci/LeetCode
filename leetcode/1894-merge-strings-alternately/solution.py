class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x = ""
        if len(word1) <= len(word2):
            for i in range(len(word1)):
                x += word1[i]
                x += word2[i]
            x += word2[len(word1):]
        else:
           for i in range(len(word2)):
                x += word1[i]
                x += word2[i]
           x += word1[len(word2):]
        return x
        
