from typing import *


class ListNode:
    """单链表实现"""
    def __init__(self, x):
        self.val = x
        self.next = None


def build_list(arr, pos):
    """环形链表的生成"""
    head = ListNode(arr[0])
    p = head
    for i in range(1, len(arr)):
        head.next = ListNode(arr[i])
        head = head.next
        if i == pos:
            temp = head
    if pos != -1:
        head.next = temp
    return p


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        题目（leetcode 142）:
        给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
        为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置
        （索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
        思考：
        环形链表考虑使用快慢指针法
        测试样例：
        >>> Solution().detectCycle(build_list([3, 2, 0, -4], 1))
        2
        """
        fast, slow = head, head
        while True:
            if not (fast and fast.next):
                return None
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast.val

    def findDuplicate(self, nums: List[int]) -> int:
        """
        题目（leetcode 287）：
        给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），
        可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
        思考：
        1). 如果仅有1个数重复出现2次，可以考虑异或(^)的思路。(X ^ X = 0, 0 ^ X = X)
        2). 建立每个值到其索引的边，由于存在重复值，因此必有环出现。(考虑快慢指针法)
        测试样例：
        >>> Solution().findDuplicate([1, 3, 4, 2, 2])
        2
        >>> Solution().findDuplicate([3, 1, 3, 4, 2])
        3
        >>> Solution().findDuplicate([1, 1])
        1
        """
        if len(nums) == 2:
            return nums[0]
        else:
            slow = nums[nums[0]]
            fast = nums[nums[nums[0]]]
            while slow != fast:
                slow = nums[slow]
                fast = nums[fast]
                fast = nums[fast]
            slow = nums[0]
            while slow != fast:
                slow = nums[slow]
                fast = nums[fast]
            return slow


if __name__ == "__main__":
    import doctest
    doctest.testmod()