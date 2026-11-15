class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combos = []
        nums.sort()
        def backtrack(i, combo):
            if i == len(nums):
                combos.append(combo[:])
                return
            combo.append(nums[i])
            backtrack(i+1, combo)
            combo.pop()
            backtrack(i+1, combo)
        backtrack(0, [])
        return combos
