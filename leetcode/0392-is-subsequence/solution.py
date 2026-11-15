class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pos = 0 #position in s
        if s == "":
            return True
        for i in range(len(t)): #go through t
            if t[i] == s[pos]: #if t = first el of s 
                pos+=1
                if pos == len(s):
                    return True
        return False
