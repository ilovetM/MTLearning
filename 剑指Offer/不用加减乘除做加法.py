"""
写一个函数，求两个整数之和，要求在函数体内不得使用 +、—、*、/ 四则运算符号
"""
# 异或以及与进位求解
# 不能一个正数一个负数

class Solution:
    def add(self, num1, num2):
        while num2 != 0:
            temp = num1 ^ num2
            print('temp', temp)
            num2 = (num1 & num2) << 1
            print('num2', num2)
            num1 = temp & 0xFFFFFFFF
            print('num1', num1)
        # 将 num1 逐渐增为 最大值

        return num1 if num1 >> 31 == 0 else num1 - 4294967296

if __name__ == '__main__':
    s = Solution()
    print(s.add(200, -15))