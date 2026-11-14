class Solution:
    def reverseWords(self, s: str) -> str:
        spl = s.split(" ")
        spl = spl[::-1]
        spl = [item for item in spl if item.strip()]
        return (" ".join(spl)).strip()
            
        
