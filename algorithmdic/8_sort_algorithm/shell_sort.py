# 希尔排序

def shell_sort(array):
    length = len(array)
    step = 2
    group = length // 2
    while group > 0:
        for i in range(0,group):
            j = i + group

            if array[i] > array[j]:
                array[i],array[j] = array[j],array[i]

        group = group // step



    pass



if __name__ == '__main__':
    a = [13,65,97,76,38,27,49]
    sorted_a = shell_sort(a)