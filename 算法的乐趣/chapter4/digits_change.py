def number2chinese(number):
    """
    题目： 将整数以中文阅读的形式输出
    限制： 0 <= number <= 1e15

    >>> number2chinese(0)
    '零'
    >>> number2chinese(1)
    '一'
    >>> number2chinese(2)
    '二'
    >>> number2chinese(3)
    '三'
    >>> number2chinese(4)
    '四'
    >>> number2chinese(5)
    '五'
    >>> number2chinese(6)
    '六'
    >>> number2chinese(7)
    '七'
    >>> number2chinese(8)
    '八'
    >>> number2chinese(9)
    '九'
    >>> number2chinese(10)
    '一十'
    >>> number2chinese(11)
    '一十一'
    >>> number2chinese(110)
    '一百一十'
    >>> number2chinese(111)
    '一百一十一'
    >>> number2chinese(100)
    '一百'
    >>> number2chinese(102)
    '一百零二'
    >>> number2chinese(1020)
    '一千零二十'
    >>> number2chinese(1001)
    '一千零一'
    >>> number2chinese(1015)
    '一千零一十五'
    >>> number2chinese(1000)
    '一千'
    >>> number2chinese(10000)
    '一万'
    >>> number2chinese(20010)
    '二万零一十'
    >>> number2chinese(20001)
    '二万零一'
    >>> number2chinese(100000)
    '一十万'
    >>> number2chinese(1000000)
    '一百万'
    >>> number2chinese(10000000)
    '一千万'
    >>> number2chinese(100000000)
    '一亿'
    >>> number2chinese(1000000000)
    '一十亿'
    >>> number2chinese(1000001000)
    '一十亿一千'
    >>> number2chinese(1000000100)
    '一十亿零一百'
    >>> number2chinese(200010)
    '二十万零一十'
    >>> number2chinese(2000105)
    '二百万零一百零五'
    >>> number2chinese(20001007)
    '二千万一千零七'
    >>> number2chinese(2000100190)
    '二十亿零一十万零一百九十'
    >>> number2chinese(1040010000)
    '一十亿四千零一万'
    >>> number2chinese(200012301)
    '二亿零一万二千三百零一'
    >>> number2chinese(2005010010)
    '二十亿零五百零一万零一十'
    >>> number2chinese(4009060200)
    '四十亿零九百零六万零二百'
    >>> number2chinese(4294967295)
    '四十二亿九千四百九十六万七千二百九十五'
    >>> number2chinese(1000000000000000)
    '一千万亿'
    """

    num2word = {"0": "零", "1": "一", "2": "二", "3": "三", "4": "四",
                "5": "五", "6": "六", "7": "七", "8": "八", "9": "九"}
    num_split = ["千", "百", "十", ""]
    num_large_split = ["万亿", "亿", "万", ""]

    def read_number_smaller_than_10000(small_number):
        ans = ""
        if len(small_number) == 4:
            for index, item in enumerate(small_number):
                if item == "0":
                    ans += num2word["0"]
                else:
                    ans += num2word[item]
                    ans += num_split[index]

        while ans[-1] == "零" and len(ans) > 1:
            ans = ans[:-1]
        if ans == "零":
            ans = ""
        return ans

    def del_zeros(s):
        s = list(s)
        for i in range(len(s) - 1, 0, -1):
            if s[i] == "零" and s[i - 1] == "零":
                s.pop(i)
        while s[0] == "零":
            s = s[1:]
        return "".join(s)

    number = str(number)
    if number == "0":
        return "零"
    if len(number) % 4 != 0:
        k = len(number) // 4 + 1
        number = "0" * (k * 4 - len(number)) + number
    else:
        k = len(number) // 4
    num_arr = []
    for i in range(k):
        num_arr.append(number[4 * i: 4 * (i + 1)])
    if len(num_arr) > 4:
        print("数字太大，无法转换")
        exit(0)
    result = ""
    for index, item in enumerate(num_arr):
        temp_ans = read_number_smaller_than_10000(item)
        if temp_ans:
            result += temp_ans
            result += num_large_split[4 - len(num_arr) + index]

    return del_zeros(result)


if __name__ == "__main__":
    import doctest
    doctest.testmod()


