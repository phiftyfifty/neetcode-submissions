class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # find a window where we can do k replacements
        char_freq = defaultdict(int)

        soln = 0
        left = 0

        for right in range(len(s)):
            char_freq[s[right]] += 1
            # calculate if the window needs to be shrunk (> k characters in right - left)
            # 
            while (right - left) - max(char_freq.values()) >= k:
                char_freq[s[left]] -= 1
                left += 1
            # calculate the window with longest repeating character here with repeating at most k replacements here 
            soln = max(right - left + 1, soln)
        return soln