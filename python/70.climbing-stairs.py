#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# @lc code=start


class Solution:
    class Stairs:
        def __init__(self):
            self.a = 2
            self.b = 3

        def __iter__(self):
            return self

        def __next__(self):
            self.a, self.b = self.b, self.a + self.b

    def climbStairs(self, n: int) -> int:
        """
        45/45 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 78.25 % of python3 submissions (17.7 MB)
        """
        if n <= 3:
            return n

        s = self.Stairs()

        for _ in range(3, n):
            next(s)

        return s.b


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        45/45 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 48.77 % of python3 submissions (17.7 MB)
        """
        a, b = 2, 3
        if n >= 3:
            for _ in range(3, n):
                a, b = b, a + b

            return b
        return n


# @lc code=end
