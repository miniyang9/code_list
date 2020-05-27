from collections import deque


def water_filter_equally(buckets_volume: list, init_status: tuple,
                         final_status: tuple, max_try=1000):
    """
    题目：
    n 个水桶平分 m 升水（一般情况 n = 3, m = 8）
    思路：
    DFS + 禁忌搜索（即对重复出现的状态剪枝）
    测试样例：
    >>> water_filter_equally([8, 5, 3], (8, 0, 0), (4, 4, 0))
    各桶的初始状态为：(8, 0, 0)
    第 1 步，从桶 0 向桶 2 倒水, 各桶的状态为：(5, 0, 3)
    第 2 步，从桶 2 向桶 1 倒水, 各桶的状态为：(5, 3, 0)
    第 3 步，从桶 0 向桶 2 倒水, 各桶的状态为：(2, 3, 3)
    第 4 步，从桶 2 向桶 1 倒水, 各桶的状态为：(2, 5, 1)
    第 5 步，从桶 1 向桶 0 倒水, 各桶的状态为：(7, 0, 1)
    第 6 步，从桶 2 向桶 1 倒水, 各桶的状态为：(7, 1, 0)
    第 7 步，从桶 0 向桶 2 倒水, 各桶的状态为：(4, 1, 3)
    第 8 步，从桶 2 向桶 1 倒水, 各桶的状态为：(4, 4, 0)
    各桶的初始状态为：(8, 0, 0)
    第 1 步，从桶 0 向桶 1 倒水, 各桶的状态为：(3, 5, 0)
    第 2 步，从桶 1 向桶 2 倒水, 各桶的状态为：(3, 2, 3)
    第 3 步，从桶 2 向桶 0 倒水, 各桶的状态为：(6, 2, 0)
    第 4 步，从桶 1 向桶 2 倒水, 各桶的状态为：(6, 0, 2)
    第 5 步，从桶 0 向桶 1 倒水, 各桶的状态为：(1, 5, 2)
    第 6 步，从桶 1 向桶 2 倒水, 各桶的状态为：(1, 4, 3)
    第 7 步，从桶 2 向桶 0 倒水, 各桶的状态为：(4, 4, 0)
    """
    def pour_water(origin: int, destination: int, status: tuple):
        if status[origin] > 0:
            water = status[origin] + status[destination]
            status_list = list(status)
            if water >= buckets_volume[destination]:
                status_list[destination] = buckets_volume[destination]
                status_list[origin] = water - buckets_volume[destination]
            else:
                status_list[destination] = water
                status_list[origin] = 0
            return tuple(status_list)
        else:
            return status

    def road_print(road_queue: deque):
        another_deque = deque()
        status, move, height = road_queue.popleft()
        another_deque.append([status, move, height])
        print(f"各桶的初始状态为：{status}")
        while road_queue:
            status, move, height = road_queue.popleft()
            another_deque.append([status, move, height])
            print(f"第 {height} 步，从桶 {move[0]} 向桶 {move[1]} 倒水, ", end="")
            print(f"各桶的状态为：{status}")
        return another_deque

    status_count = 1
    status_dict = {init_status: 0}
    search_stack = deque([[init_status, [], 0]])
    road_stack = deque()
    while search_stack and max_try > 0:
        buckets_status, __, tree_height = search_stack.pop()
        if not road_stack or road_stack[-1][-1] < tree_height:
            road_stack.append([buckets_status, __, tree_height])
        else:
            while road_stack[-1][-1] >= tree_height:
                road_stack.pop()
            road_stack.append([buckets_status, __, tree_height])
        if buckets_status == final_status:
            # 当出现最终状态时，输出可行路径
            road_stack = road_print(road_stack)
            status_dict.pop(final_status)
            if not search_stack:
                break
            buckets_status, __, tree_height = search_stack.pop()
            if not road_stack or road_stack[-1][-1] < tree_height:
                road_stack.append([buckets_status, __, tree_height])
            else:
                while road_stack[-1][-1] >= tree_height:
                    road_stack.pop()
                road_stack.append([buckets_status, __, tree_height])
        for i in range(len(buckets_status)):
            for j in range(i + 1, len(buckets_status)):
                temp_status = pour_water(i, j, buckets_status)
                if temp_status not in status_dict:
                    # 当且仅当当前字典中不存在该状态时，记录为有效状态
                    status_dict[temp_status] = status_count
                    status_count += 1
                    search_stack.append([temp_status, [i, j], tree_height + 1])
                temp_status = pour_water(j, i, buckets_status)
                if temp_status not in status_dict:
                    status_dict[temp_status] = status_count
                    status_count += 1
                    search_stack.append([temp_status, [j, i], tree_height + 1])

        max_try -= 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()



