from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(N log k) time
        # O(N) space
        counts = Counter(nums)

        heap = []  # min-heap of (freq, num), kept at size k
        for num, freq in counts.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)  # drop the least frequent
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result