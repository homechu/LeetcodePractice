#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# # @lc code=start
class Solution:
    def numIslands(self, grid) -> int:
        """
        49/49 cases passed (229 ms)
        Your runtime beats 93.03 % of python3 submissions
        Your memory usage beats 95.52 % of python3 submissions (20 MB)
        """
        res = 0
        de, we = len(grid), len(grid[0])

        def dfs(i, j):
            deque = [(i, j)]
            while deque:
                r, c = deque.pop()
                for raw, col in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    i, j = r + raw, c + col
                    if (0 <= i < de) and (0 <= j < we) and grid[i][j] == "1":
                        deque.append((i, j))
                        grid[i][j] = "0"

        for i in range(de):
            for j in range(we):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    dfs(i, j)
                    res += 1
        return res


class Solution:
    """"""

    def numIslands(self, grid) -> int:
        """
        49/49 cases passed (238 ms)
        Your runtime beats 79.17 % of python3 submissions
        Your memory usage beats 69.08 % of python3 submissions (20.1 MB)
        """
        if not grid:
            return 0

        res = 0
        de, we = len(grid), len(grid[0])

        def bfs(i, j):
            deque = [(i, j)]
            while deque:
                r, c = deque.pop()

                for raw, col in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    x, y = r + raw, c + col
                    if (0 <= x < de) and (0 <= y < we) and grid[x][y] == "1":
                        grid[x][y] = "0"
                        deque.append((x, y))

        for i in range(de):
            for j in range(we):
                if grid[i][j] == "1":
                    res += 1
                    bfs(i, j)

        return res


# @lc code=end
