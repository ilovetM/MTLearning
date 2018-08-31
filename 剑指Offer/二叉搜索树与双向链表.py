"""
输入一颗二叉搜索树，将二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的节点，只能调整树中节点指针的指向。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convert(self, node):
        if node is None:
            return None
        if node.left and node.right is None:
            return node

        # 处理左子树
        self.convert(node.left)
        left = node.left

        # 连接根与左子树最大节点
        if left:
            while left.right:
                left = left.right
            node.left, left.right = left, node

        self.convert(node.right)
        right = node.right

        # 连接根与有字数最小节点
        if right:
            while right.left:
                right = right.left
            node.right, right.left = right, node

        while node.left:
            node = node.left
        return node


if __name__ == '__main__':

    pNode1 = TreeNode(8)
    pNode2 = TreeNode(6)
    pNode3 = TreeNode(10)
    pNode4 = TreeNode(5)
    pNode5 = TreeNode(7)
    pNode6 = TreeNode(9)
    pNode7 = TreeNode(11)

    pNode1.left = pNode2
    pNode1.right = pNode3
    pNode2.left = pNode4
    pNode2.right = pNode5
    pNode3.left = pNode6
    pNode3.right = pNode7

    S = Solution()
    newList = S.convert(pNode1)
    print(newList.val)
    while newList.right:
        newList = newList.right
        print(newList.val)
