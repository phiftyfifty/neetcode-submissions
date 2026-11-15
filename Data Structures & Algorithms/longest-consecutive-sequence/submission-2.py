class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hash_set = defaultdict(int)
        lcs = 0

        for i in range(len(nums)):
            if not hash_set[nums[i]]:
                # set current
                hash_set[nums[i]] = hash_set[nums[i]-1] + hash_set[nums[i]+1] + 1
                hash_set[nums[i]- hash_set[nums[i] - 1]] = hash_set[nums[i]]
                hash_set[nums[i]+ hash_set[nums[i] + 1]] = hash_set[nums[i]]
                lcs = max(hash_set[nums[i]], lcs)
        return lcs