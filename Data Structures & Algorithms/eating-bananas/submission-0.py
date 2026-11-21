class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0

        while l <= r:
            mp = l + (r - l) // 2
            hrs = 0
            for p in piles:
                hrs += math.ceil(float(p) / mp)
            if hrs <= h:
                r = mp - 1
                res = mp
            else:
                l = mp + 1
        return res