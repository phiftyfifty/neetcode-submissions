class Solution:
    def trap(self, height: List[int]) -> int:
        map_area = defaultdict(int)
        area = 0
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        while left <= right: 
            max_left = max(height[left], max_left)
            max_right = max(height[right], max_right)

      
            if max_left < max_right: 
                area += max(0, max_left - height[left])
                left += 1
            else:
                area += max(0, max_right - height[right])
                right -= 1
        return area
