class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for start, end in intervals:
            prev_end = result[-1][1]
            # can be overlapping
            if prev_end >= start:
                result[-1][1] = max(end, prev_end)
            # separate interval
            else:
                result.append([start, end])
        return result