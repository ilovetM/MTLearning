#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself 
             according to the LCA definition.
             
Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if p.val > q.val:
            p, q = q, p
        ancestor = root

        if p.val == ancestor.val:
            return p.val
        if q.val == ancestor.val:
            return q.val

        if p.val < ancestor.val and q.val > ancestor.val:
            return ancestor
        elif p.val > ancestor.val:
            return self.lowestCommonAncestor(ancestor.right, p, q)
        elif q.val < ancestor.val:
            return self.lowestCommonAncestor(ancestor.left, p, q)

if __name__ == '__main__':
    tr = TreeNode

    root = tr(6)
    # root.
    tree = tr(6, tr(2, tr(0), tr(4, tr(3), tr(5))), tr(8, tr(7), tr(9)))
    solution = Solution()
    print(solution.lowestCommonAncestor(tree, 2, 8))
    print(solution.lowestCommonAncestor(tree, 2, 4))