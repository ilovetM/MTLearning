# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        output = [self.val]
        n = self.next
        while n is not None:
            output.append(n.val)
            n = n.next
        return '=>'.join(map(str, output))


class Solution:
    @classmethod
    def reverse_list(cls, head):
        new_head = None
        while head is not None:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
        return new_head

    @classmethod
    def reverse_list_recursive(cls, head):
        if head is None or head.next is None:
            return head

        p = head.next
        n = cls.reverse_list_recursive(p)

        head.next = None
        p.next = head
        return n


if __name__ == '__main__':
    a, b, c, d, e = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    print(a)
    # print(Solution.reverse_list(a))
    print(Solution.reverse_list_recursive(a))
