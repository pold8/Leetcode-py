class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        reversed = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            d = x % 10
            x //= 10

            if reversed > INT_MAX // 10 or (reversed == INT_MAX // 10 and d > 7):
                return 0

            reversed = reversed * 10 + d

        return reversed * sign