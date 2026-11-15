class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        mp = {}
        left = 0
        n = len(s)
        lcs = 0
        r = 0

        while r < n:
            # progress left if right is a duplicate
            if s[r] in mp:
                left = max(mp[s[r]] + 1, left)
            # indicate count at position
            mp[s[r]] = r 
            lcs = max(lcs, r - mp[s[left]] + 1)
            r += 1
        return lcs
            
            