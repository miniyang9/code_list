from typing import *


class Solution:
    """
    题目（leetcode 978）：
    当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组：
    若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
    或若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]
    也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组
    返回 A 的最大湍流子数组的长度
    思路：
    用 dp[i][0] 表示以 i 结尾的最长湍流子数组, dp[i][1] 表示第 i - 1 个数和第 i 个数
    的大小关系
    那么，当 nums[i + 1] > nums[i], 且 dp[i][1] 为 "<" 时， 将长度加 1
    当 nums[i + 1] < nums[i]， 且 dp[i][1] 为 "<" 时， 将长度更新为 2
    当 nums[i + 1] = nums[i]， 将长度更新为 1
    测试样例：
    >>> Solution().maxTurbulenceSize([9,4,2,10,7,8,8,1,9])
    5
    >>> Solution().maxTurbulenceSize([4,8,12,16])
    2
    >>> Solution().maxTurbulenceSize([100])
    1
    """
    def maxTurbulenceSize(self, A: List[int]) -> int:
        # dp = [1, ""]
        # max_length = dp[0][0]
        # for i in range(1, len(A)):
        #     if A[i] > A[i - 1]:
        #         if dp[-1][1] != ">":
        #             dp.append([dp[-1][0] + 1, ">"])
        #         else:
        #             dp.append([2, ">"])
        #     elif A[i] < A[i - 1]:
        #         if dp[-1][1] != "<":
        #             dp.append([dp[-1][0] + 1, "<"])
        #         else:
        #             dp.append([2, "<"])
        #     else:
        #         dp.append([1, "="])
        #     if max_length < dp[-1][0]:
        #         max_length = dp[-1][0]
        # return max_length

        # 优化后：
        dp = [1, ""]
        max_length = dp[0]
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                if dp[1] != ">":
                    dp = [dp[0] + 1, ">"]
                else:
                    dp = [2, ">"]
            elif A[i] < A[i - 1]:
                if dp[1] != "<":
                    dp = [dp[0] + 1, "<"]
                else:
                    dp = [2, "<"]
            else:
                dp = [1, "="]
            if max_length < dp[0]:
                max_length = dp[0]
        return max_length


if __name__ == "__main__":
    import doctest
    doctest.testmod()
