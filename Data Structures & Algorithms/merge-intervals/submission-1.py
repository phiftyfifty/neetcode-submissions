class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []

        for i, j in intervals:
            if not result:
                result.append([i, j])
            prev_j = result[-1][1]
            # can possibly be merged
            if i <= prev_j:
                result[-1][1] = max(prev_j, j)
            else:
                # separate interval
                result.append([i, j])
        return result