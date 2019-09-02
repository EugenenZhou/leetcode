# 归并排序，递增左右比较，时间：O(nlogn);空间：O(1)。

def merge_sort(array):
    def merge(left,right): # 合并
        i,j = 0,0
        res = []
        l = len(left)
        r = len(right)
        while i < l and j < r:
            if left[i] < right[j]:
                res.append(left[i])
                i = i + 1
            else:
                res.append(right[j])
                j = j + 1
        res = res + left[i::]
        res = res + right[j::]
        return res
    if len(array) <= 1:
        return array
    num = len(array) // 2
    left = merge_sort(array[0:num]) # 左分支
    right = merge_sort(array[num::]) # 右分支
    return merge(left,right)



if __name__ == '__main__':
    a = [13,65,97,76,38,27,49]
    sorted_a = merge_sort(a)