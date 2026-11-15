class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lcp = 1
        prefix = [1] * len(nums)

        for i in range(len(nums)):
            prefix[i] = lcp 
            lcp *= nums[i]
        lcp = 1
        # [1, 1, 2, 8]
        # [_ _ _ 4]
        for j in range(len(nums) - 1, -1, -1):
            prefix[j] *= lcp
            lcp *= nums[j]
        return prefix
        