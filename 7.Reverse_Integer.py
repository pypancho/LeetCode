class Solution:
    def reverse(self, x: int) -> int:
        a = 0

        if x > 0:
            while (x > 0):
                a = a * 10 + (x % 10)
                x = x // 10
        else:
            x = 0 - x
            while (x > 0):
                a = a * 10 + (x % 10)
                x = x // 10
            a = 0 - a
        if a < -2147483648 or a > 2147483647:
            return 0
        else:
            return a
