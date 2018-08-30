"""
输入两个链表，找出它们的第一个公共节点
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def compute_length(node):
        length = 0
        while node is not None:
            node = node.next
            length += 1
        return length

    def find_first_common_node(self, left, right):
        l_length, r_length = self.compute_length(left), self.compute_length(right)
        length_diff = abs(l_length - r_length)

        if l_length > r_length:
            long, short = left, right
        else:
            long, short = right, left

        for i in range(length_diff):
            long = long.next

        while long is not None and short is not None and long != short:
            long = long.next
            short = short.next

        return long
