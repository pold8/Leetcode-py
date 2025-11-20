class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ap = set()
        left = 0
        maxLen = 0

        for right in range(len(s)):
            while s[right] in ap:
                ap.remove(s[left])
                left += 1
            ap.add(s[right])
            maxLen = max(maxLen, right - left + 1)

        return maxLen