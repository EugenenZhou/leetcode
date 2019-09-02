# 插入排序，按序遍历将数组元素置于正确位置，时间：O(n)-O(n^2);空间：O(1)。

def insert_sort(array):
    length = len(array)
    for i in range(1,length):
        j = i
        while j > 0:
            if array[j] < array[j-1]:
                array[j],array[j-1] = array[j-1],array[j]
                j = j - 1
            else:
                break
        print(array)
    return array



if __name__ == '__main__':
    a = [13,65,97,76,38,27,49]
    sorted_a = insert_sort(a)