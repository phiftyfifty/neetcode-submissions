class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parents = {"{": "}", "[": "]", "(": ")"}

        for ch in s:
            if ch in parents:
                stack.append(ch)
            else:
                if stack and ch == parents[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
