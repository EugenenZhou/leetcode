# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，返回它的最大深度 3 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

######################################################################
# 递归
def maxDepth(root):
    if root == None:
        return 0
    return max(maxDepth(root.left),maxDepth(root.right))+1

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

tree = '[3,9,20,null,null,15,7]'
Tree = stringToTreeNode(tree)
result = maxDepth(Tree)
print(result)





