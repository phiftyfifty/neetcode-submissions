class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        middle_idx = len(s) // 2
        # optimal: O(N) time and O(1) space
        # two pointer approach, start from the middle index and expand outward
        for i in range(len(s) // 2):
            # odd length 
            if len(s) % 2 == 1:
                if s[middle_idx+i-1] != s[middle_idx-i+1]:
                    return False
            # even length
            # aab
            else:
                if s[middle_idx-i-1] != s[middle_idx+i]:
                    print(i)
                    return False

        return True