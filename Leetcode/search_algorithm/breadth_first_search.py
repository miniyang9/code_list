from typing import *
from collections import deque


class Solution:
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
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()

