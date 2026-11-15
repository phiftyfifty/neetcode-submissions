class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left, right = 0, len(numbers) - 1

        for i in range(len(numbers)):
            tmp = target - numbers[i]
            left, right = i + 1, len(numbers) - 1 
            while left <= right:
                m_p = left + (right - left) // 2
                if numbers[m_p] == tmp:
                    return [i+1, m_p + 1]
                elif numbers[m_p] > tmp:
                    right = m_p - 1
                else:
                    left = m_p + 1
        return []
        