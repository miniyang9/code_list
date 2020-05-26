from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    # 利用层序构建树
    def __init__(self, arr):
        if arr:
            temp_list = []
            for item in arr:
                if item:
                    temp_list.append(TreeNode(item))
                else:
                    temp_list.append(None)
            for index in range(int(len(arr) / 2)):
                if temp_list[index] is not None:
                    temp_list[index].left = temp_list[index * 2 + 1]
                    if index * 2 + 2 < len(arr):
                        temp_list[index].right = temp_list[index * 2 + 2]
            self.root = temp_list[0]
        else:
            self.root = None


class Solution:
    def __init__(self):
        self.flag = True

    def isBalanced(self, root: TreeNode) -> bool:
        """
        题目（leetcode 110）：
        实现一个函数，检查二叉树是否平衡。
        在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。
        思考：
        dfs探查每个节点左右子树的高度差是否大于1
        测试样例：
        >>> Solution().isBalanced(Tree([1, None, 2, None, None, None, 3]).root)
        False
        >>> Solution().isBalanced(Tree([]).root)
        True
        >>> Solution().isBalanced(Tree([1, 2, 2, 3, 3]).root)
        True
        >>> Solution().isBalanced(Tree([1, 2, 2, 3, 3, None, None, 4, 4]).root)
        False
        """
        def isb(node):
            if not node:
                return 0
            l = isb(node.left) + 1
            r = isb(node.right) + 1
            if abs(l - r) > 1:
                self.flag = False
            return max(l, r)
        isb(root)
        return self.flag

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """
        题目（leetcode 529）:
        给定一个代表游戏板的二维字符矩阵。 
        'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，
        'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，
        数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，
        'X' 则表示一个已挖出的地雷。

        现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），
        根据以下规则，返回相应位置被点击后对应的面板：

        1.如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
        2.如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），
        并且所有和其相邻的方块都应该被递归地揭露。
        3.如果一个至少与一个地雷相邻的空方块（'E'）被挖出，
        修改它为数字（'1'到'8'），表示相邻地雷的数量。
        4.如果在此次点击中，若无更多方块可被揭露，则返回面板。
        思路：
        将每个'B'周围的格子放入到栈中
        测试样例：
        >>> a = [['E', 'E', 'E', 'E', 'E'],
        ... ['E', 'E', 'M', 'E', 'E'],
        ... ['E', 'E', 'E', 'E', 'E'],
        ... ['E', 'E', 'E', 'E', 'E']]
        >>> click = [3, 0]
        >>> Solution().updateBoard(a, click)
        [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
        """
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        m, n = len(board) - 1, len(board[0]) - 1
        stack = [click]
        while stack:
            x, y = stack.pop()
            count = 0
            if board[x][y] == "E":
                if 0 <= x - 1 <= m and 0 <= y - 1 <= n:
                    if board[x - 1][y - 1] == "M":
                        count += 1
                if 0 <= y - 1 <= n:
                    if board[x][y - 1] == "M":
                        count += 1
                if 0 <= x - 1 <= m:
                    if board[x - 1][y] == "M":
                        count += 1
                if 0 <= x + 1 <= m and 0 <= y + 1 <= n:
                    if board[x + 1][y + 1] == "M":
                        count += 1
                if 0 <= y + 1 <= n:
                    if board[x][y + 1] == "M":
                        count += 1
                if 0 <= x + 1 <= m:
                    if board[x + 1][y] == "M":
                        count += 1
                if 0 <= x - 1 <= m and 0 <= y + 1 <= n:
                    if board[x - 1][y + 1] == "M":
                        count += 1
                if 0 <= x + 1 <= m and 0 <= y - 1 <= n:
                    if board[x + 1][y - 1] == "M":
                        count += 1
                if count == 0:
                    board[x][y] = "B"
                    if 0 <= x - 1 <= m and 0 <= y - 1 <= n:
                        if board[x - 1][y - 1] == "E":
                            stack.append([x - 1, y - 1])
                    if 0 <= y - 1 <= n:
                        if board[x][y - 1] == "E":
                            stack.append([x, y - 1])
                    if 0 <= x - 1 <= m:
                        if board[x - 1][y] == "E":
                            stack.append([x - 1, y])
                    if 0 <= x + 1 <= m and 0 <= y + 1 <= n:
                        if board[x + 1][y + 1] == "E":
                            stack.append([x + 1, y + 1])
                    if 0 <= y + 1 <= n:
                        if board[x][y + 1] == "E":
                            stack.append([x, y + 1])
                    if 0 <= x + 1 <= m:
                        if board[x + 1][y] == "E":
                            stack.append([x + 1, y])
                    if 0 <= x - 1 <= m and 0 <= y + 1 <= n:
                        if board[x - 1][y + 1] == "E":
                            stack.append([x - 1, y + 1])
                    if 0 <= x + 1 <= m and 0 <= y - 1 <= n:
                        if board[x + 1][y - 1] == "E":
                            stack.append([x + 1, y - 1])
                else:
                    board[x][y] = str(count)
        return board


if __name__ == "__main__":
    import doctest
    doctest.testmod()
