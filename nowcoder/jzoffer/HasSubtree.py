# 树的子结构

# 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

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
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False
        return self.classifytree(pRoot1,pRoot2) or self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)
    def classifytree(self, tree1,tree2):
        if not tree2:
            return True
        if not tree1 or tree1.val != tree2.val:
            return False
        return self.classifytree(tree1.left,tree2.left) and self.classifytree(tree1.right,tree2.right)
        # write code here

######################################################################
tree = '[3,9,20,null,null,15,7]'
Btree = stringToTreeNode(tree)