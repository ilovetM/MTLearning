"""
把只包含因子2、3和5的数称作丑数。例如6、8都是丑数，但14不是，因为他包含因子7.
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""


class Solution:
    def get_ugly_number(self, index):
        if index is None or index <= 0:
            return 0

        ugly_numbers = [1] * index
        next_index = 1

        index2 = 0
        index3 = 0
        index5 = 0

        while next_index < index:
            min_val = min(ugly_numbers[index2] * 2, ugly_numbers[index3] * 3, ugly_numbers[index5] * 5)
            ugly_numbers[next_index] = min_val

            while ugly_numbers[index2] * 2 <= ugly_numbers[next_index]:
                index2 += 1
            while ugly_numbers[index3] * 3 <= ugly_numbers[next_index]:
                index3 += 1

            while ugly_numbers[index5] * 5 <= ugly_numbers[next_index]:
                index5 += 1

            next_index += 1
        return ugly_numbers[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.get_ugly_number(12))
    print(s.get_ugly_number(13))
    print(s.get_ugly_number(24))
    print(s.get_ugly_number(66))