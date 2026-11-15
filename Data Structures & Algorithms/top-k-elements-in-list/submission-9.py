class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(N) time
        # O(N) space
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # count: freq
        for num, count in count.items():
            freq[count].append(num)

        result = []
        # Start from the most frequent, down to the least frequent 
        for i in range(len(freq) - 1, 0, -1):
            for number in freq[i]:
                result.append(number)
                # return once result has k numbers
                if len(result) == k:
                    return result
        return result