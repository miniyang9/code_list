from typing import *
from collections import deque


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        题目（Leetcode 542）：
        给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
        两个相邻元素间的距离为 1（仅上下左右）
        思路：
        1）顺序遍历，将非0元素更新为当前元素周围最小元素值加1，直到不在修改
        2）BFS，依次填充距离0元素距离为1，2，3。。。的位置
        测试样例：
        >>> m = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        >>> Solution().updateMatrix(m)
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        >>> m = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
        >>> Solution().updateMatrix(m)
        [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
        """
        dq = deque()
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    dq.append([i, j, 0])
                else:
                    matrix[i][j] = -1
        while dq:
            x, y, count = dq.popleft()
            if 0 <= x - 1 <= m and matrix[x - 1][y] == -1:
                matrix[x - 1][y] = count + 1
                dq.append([x - 1, y, count + 1])
            if 0 <= x + 1 <= m and matrix[x + 1][y] == -1:
                matrix[x + 1][y] = count + 1
                dq.append([x + 1, y, count + 1])
            if 0 <= y - 1 <= n and matrix[x][y - 1] == -1:
                matrix[x][y - 1] = count + 1
                dq.append([x, y - 1, count + 1])
            if 0 <= y + 1 <= n and matrix[x][y + 1] == -1:
                matrix[x][y + 1] = count + 1
                dq.append([x, y + 1, count + 1])

        return matrix

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        题目（leetcode 200）：
        给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
        岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
        此外，你可以假设该网格的四条边均被水包围
        思路：
        BFS 或 DFS 均可
        这里用 BFS 实现，利用队列进行搜索
        测试样例：
        >>> Solution().numIslands([["1", "1", "0", "0", "0"],
        ... ["1", "1", "0", "0", "0"],
        ... ["0", "0", "1", "0", "0"],
        ... ["0", "0", "0", "1", "1"]])
        3
        >>> Solution().numIslands([["1", "1", "1", "1", "0"],
        ... ["1", "1", "0", "1", "0"],
        ... ["1", "1", "0", "0", "0"],
        ... ["0", "0", "0", "0", "0"]])
        1
        """
        if not grid:
            return 0
        count = 0
        dq = deque()
        all_island = []
        m, n = len(grid) - 1, len(grid[0]) - 1
        for i in range(m + 1):
            for j in range(n + 1):
                if grid[i][j] == "1":
                    all_island.append([i, j])
        while all_island:
            x, y = all_island.pop()
            if grid[x][y] == "1":
                count += 1
                dq.append([x, y])
                while dq:
                    i, j = dq.popleft()
                    grid[i][j] = "-1"
                    if 0 <= i - 1 <= m:
                        if grid[i - 1][j] == "1":
                            grid[i - 1][j] = "-1"
                            dq.append([i - 1, j])
                    if 0 <= i + 1 <= m:
                        if grid[i + 1][j] == "1":
                            grid[i + 1][j] = "-1"
                            dq.append([i + 1, j])
                    if 0 <= j - 1 <= n:
                        if grid[i][j - 1] == "1":
                            grid[i][j - 1] = "-1"
                            dq.append([i, j - 1])
                    if 0 <= j + 1 <= n:
                        if grid[i][j + 1] == "1":
                            grid[i][j + 1] = "-1"
                            dq.append([i, j + 1])
                    # if 0 <= i - 1 <= m and 0 <= j - 1 <= n:
                    #     if grid[i - 1][j - 1] == "1":
                    #         grid[i - 1][j - 1] = "-1"
                    #         dq.append([i - 1, j - 1])
                    # if 0 <= i + 1 <= m and 0 <= j - 1 <= n:
                    #     if grid[i + 1][j - 1] == "1":
                    #         grid[i + 1][j - 1] = "-1"
                    #         dq.append([i + 1, j - 1])
                    # if 0 <= i - 1 <= m and 0 <= j + 1 <= n:
                    #     if grid[i - 1][j + 1] == "1":
                    #         grid[i - 1][j + 1] = "-1"
                    #         dq.append([i - 1, j + 1])
                    # if 0 <= i + 1 <= m and 0 <= j + 1 <= n:
                    #     if grid[i + 1][j + 1] == "1":
                    #         grid[i + 1][j + 1] = "-1"
                    #         dq.append([i + 1, j + 1])
        return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()
