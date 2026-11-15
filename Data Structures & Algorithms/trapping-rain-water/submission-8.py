class Solution:
    def trap(self, height: List[int]) -> int:
        # 
        max_areas = defaultdict(int)
        area = 0
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        while left <= right: 
            max_left = max(height[left], max_left)
            max_right = max(height[right], max_right)

      
            if max_left < max_right:      
                max_areas[left] = max(0, max_left - height[left])
                area += max_areas[left]
                left += 1
            else:
                max_areas[right] = max(0, max_right - height[right])
                area += max_areas[right]
                right -= 1
        return area
