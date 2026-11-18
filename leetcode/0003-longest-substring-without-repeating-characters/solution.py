class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest_sub = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            longest_sub = max(longest_sub, len(seen))
        return longest_sub


