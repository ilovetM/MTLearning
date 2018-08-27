"""
把n个骰子扔在地上，所有骰子朝上面的点数和为s。
输入n，打印出s的所有可能值出现的概率
"""


# 基于循环求点数，时间性能好。。。。？？？
def compute_possibility(number):
    if number < 1:
        return
    max_value = 6
    total_range = max_value * number + 1
    # 构造两个数组来存储骰子点数的每一个总数出现的次数
    # 第一次循环，第一个数组中的第n个数字表示骰子和为n出现的次数
    # 在第二次循环中，另一个数组的第n个数字设为前一个数组对应的第n-1、n-2、n-3、n-4、n-5、n-6之和
    possi_storage = [[], []]
    possi_storage[0] = [0] * total_range  # 最大容量
    flag = 0
    for i in range(1, max_value + 1):
        possi_storage[flag][i] = 1
    for time in range(2, number + 1):
        possi_storage[1 - flag] = [0] * total_range
        for p in range(time, total_range):
            dice_num = 1
            while dice_num < p and dice_num <= max_value:
                possi_storage[1 - flag][p] += possi_storage[flag][p - dice_num]
                dice_num += 1
        flag = 1 - flag
    total = max_value ** number
    for i in range(number, total_range):
        ratio = possi_storage[flag][i] / float(total)
        print("{}: {:e}".format(i, ratio))

if __name__ == '__main__':
    s = compute_possibility(5)
