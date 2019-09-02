# 选择排序，选一个最小的和第一个交换，反复如是，时间：O(n^2);空间：O(1)。

def select_sort(array):
    for i in range(len(array)):
        index = i
        for j in range(i+1,len(array)):
            if array[j] < array[index]:
                index = j
        array[i],array[index] = array[index],array[i]
        print(array)
    return array



if __name__ == '__main__':
    a = [13,65,97,76,38,27,49]
    sorted_a = select_sort(a)




