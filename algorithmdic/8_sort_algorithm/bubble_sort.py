# 冒泡排序，冒泡式递增左右比较，时间：O(n)-O(n^2);空间：O(1)。

def bubble_sort(array):
    length = len(array)
    change = 1
    while change > 0 and length > 1:
        change = 0
        for i in range(0,length-1):
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
                change = change + 1
        length = length - 1
        print(array)
    return array



if __name__ == '__main__':
    a = [13,65,97,76,38,27,49]
    sorted_a = bubble_sort(a)