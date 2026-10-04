class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        reversed = ""
        for i in range(len(s)):
            if (s[i].lower() in "aeiou"):
                vowels.append(s[i])
        for i in range(len(s)):
            if (s[i].lower() in "aeiou"):
                reversed+= vowels[-1]
                vowels.pop()
            else:
                reversed+=s[i]
        return reversed
