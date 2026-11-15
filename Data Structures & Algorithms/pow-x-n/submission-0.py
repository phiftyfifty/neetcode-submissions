class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        else:
            if n > 0:
                return self.myPow(x, n-1) * x
            if n < 0:
                x = 1 / x * self.myPow(x, n+1) 
                return x