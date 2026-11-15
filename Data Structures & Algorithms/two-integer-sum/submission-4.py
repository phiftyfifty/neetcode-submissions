class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}

        for i in range(len(nums)):
            if target - nums[i] in hash_table and hash_table[target-nums[i]] != i:
                return [min(hash_table[target-nums[i]], i), max(hash_table[target-nums[i]], i)]
            hash_table[nums[i]] = i
        print(target)
        return []
                