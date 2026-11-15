class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        increment_dct = defaultdict(int)
        lcs = 0
        for i in range(len(nums)):
            if not increment_dct[nums[i]]:
                increment_dct[nums[i]] = increment_dct[nums[i] - 1] + increment_dct[nums[i] + 1] + 1
                # num | cur | num
                increment_dct[nums[i] - increment_dct[nums[i] - 1]] = increment_dct[nums[i]]
                increment_dct[nums[i] + increment_dct[nums[i] + 1]] = increment_dct[nums[i]]
                lcs = max(lcs, increment_dct[nums[i]])
            
        return lcs