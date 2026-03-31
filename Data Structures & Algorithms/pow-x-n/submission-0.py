class Solution:
    def myPow(self, x: float, n: int) -> float:
        mul = n > 0
        sumTotal = 1
        if mul:
            for i in range(n):
                sumTotal *= x
        else:
            for i in range(abs(n)):
                sumTotal /= x
        return sumTotal