class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length <= 2:
            return 0
        max_area = 0

        for i in range(length):
            left_max = right_max = height[i]
            
            for j in range(i):
                left_max = max(left_max, height[j])
            for j in range(i+1, length):
                right_max = max(right_max, height[j])

            max_area += min(right_max - height[i], left_max - height[i])
        return max_area

