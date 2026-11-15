from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        min_window = float('inf')
        freq_t = Counter(t)
        min_window_dct = {}
        left = 0
        num_matches = 0
        answer = ""
        for right in range(len(s)):
            min_window_dct[s[right]] = min_window_dct.get(s[right], 0) + 1

            if min_window_dct[s[right]] == freq_t[s[right]]:
                num_matches += 1

            while left <= right and len(freq_t) == num_matches:
                if right - left + 1 < min_window:
                    answer = s[left:right+1]
                    min_window = right - left + 1
                min_window_dct[s[left]] -= 1
                if min_window_dct[s[left]] < freq_t[s[left]]:
                    num_matches -= 1
                left += 1

        return answer