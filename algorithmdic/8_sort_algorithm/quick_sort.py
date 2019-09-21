# 快速排序，基准点左右交换，有序时效果变为冒泡排序，时间：O(nlogn)-O(n^2);空间：O(logn)。

def quick_sort(array,left,right):
    if left >= right:
        return array
    key = array[left]
    low = left
    high = right
    while left < right:
        while left < right and array[right] >= key:
            right = right - 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left = left + 1
        array[right] = array[left]
    array[right] = key
    quick_sort(array,low,right-1)
    quick_sort(array,right+1,high)
    return array



if __name__ == '__main__':
    a = [13,65,97,76,38,27,49]
    sorted_a = quick_sort(a,0,len(a)-1)
