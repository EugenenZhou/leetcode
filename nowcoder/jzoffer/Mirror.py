# 二叉树的镜像

# 操作给定的二叉树，将其变换为源二叉树的镜像。

######################################################################
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root
######################################################################
# -*- coding:utf-8 -*-
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root != None:
            root.left,root.right = root.right,root.left
            self.Mirror(root.left)
            self.Mirror(root.right)
       # write code here

######################################################################
tree = '[3,9,20,null,null,15,7]'
Btree = stringToTreeNode(tree)