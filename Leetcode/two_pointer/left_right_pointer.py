from typing import *


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        题目（leetcode 11）：
        给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
        在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
        找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
        思路：
        左右指针法
        每次将对应的数字较小的那个指针，
        往另一个指针的方向移动一个位置，
        因为这个指针不可能再作为容器的边界了。
        测试样例：
        >>> Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
        49
        """
        i, j = 0, len(height) - 1
        area = []
        while i != j:
            area.append(min(height[i], height[j]) * (j - i))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return max(area)

    def trap(self, height: List[int]) -> int:
        """
        题目（leetcode 42）:
        给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，
        计算按此排列的柱子，下雨之后能接多少雨水
        思路：
        左右指针法
        所以我们可以认为如果一端有更高的条形块（例如右端），
        积水的高度依赖于当前方向的高度（从左到右）。
        当我们发现另一侧（右侧）的条形块高度不是最高的，
        我们则开始从相反的方向遍历（从右到左）。
        我们必须在遍历时维护 left_max 和 right_max ，
        但是我们现在可以使用两个指针交替进行，实现 1 次遍历即可完成。
        测试样例：
        >>> Solution().trap([])
        0
        >>> Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
        6
        """
        if not height:
            return 0
        left_max, right_max = 0, 0
        left, right = 0, len(height) - 1
        water = 0
        while left != right:
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water


if __name__ == "__main__":
    import doctest
    doctest.testmod()
