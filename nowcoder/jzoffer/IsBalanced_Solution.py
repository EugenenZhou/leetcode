# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        if abs(self.Maxdepth(pRoot.left)-self.Maxdepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
    def Maxdepth(self,pRoot):
        if not pRoot:
            return 0
        left = self.Maxdepth(pRoot.left) + 1
        right = self.Maxdepth(pRoot.right) + 1
        return max(left,right)
        # write code here