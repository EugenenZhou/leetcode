# 二叉搜索树的后序遍历

# 输入一个整数数组，
# 判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
######################################################################
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence == []:
            return False
        if self.classify(sequence,0,len(sequence)-1):
            return True
        else:
            return False
    def classify(self,sequence,start,end):
        if start >= end:
            return True
        root = sequence[end]
        i = 0
        while i < end:
            if sequence[i] > root:
                break
            i = i + 1
        j = i
        while j < end:
            if sequence[j] < root:
                return False
            j = j + 1
        l = True
        if i > start:
            l = self.classify(sequence,start,i-1)
        r = True
        if i < end:
            r = self.classify(sequence,i,end-1)
        return (r and l)



# write code here
######################################################################
bst = [7,4,6,5]
s = Solution()
result = s.VerifySquenceOfBST(bst)
print(result)





