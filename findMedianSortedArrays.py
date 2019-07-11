# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
# 你可以假设 nums1 和 nums2 不会同时为空。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
######################################################################
def findMedianSortedArrays(nums1, nums2):
    length = len(nums1) + len(nums2)
    all = []
    if length % 2 == 0:
        if nums1.__len__() == 0:
            midnum = (nums2[length // 2 - 1] + nums2[length // 2]) / 2
        elif nums2.__len__() == 0:
            midnum = (nums1[length // 2 - 1] + nums1[length // 2]) / 2
        else:
            # 排序
            n1 = n2 = 0
            for i in range(0, length // 2 + 1):
                if n1 == nums1.__len__():
                    all.append(nums2[n2])
                    n2 = n2 + 1
                elif n2 == nums2.__len__():
                    all.append(nums1[n1])
                    n1 = n1 + 1
                else:
                    if nums1[n1] <= nums2[n2]:
                        all.append(nums1[n1])
                        n1 = n1 + 1
                    else:
                        all.append(nums2[n2])
                        n2 = n2 + 1
            midnum = (all[length // 2 - 1] + all[length // 2]) / 2

    else:
        if nums1.__len__() == 0:
            midnum = nums2[length // 2]
        elif nums2.__len__() == 0:
            midnum = nums1[length // 2]
        else:
            # 排序
            n1 = n2 = 0
            for i in range(0, length // 2 + 1):
                if n1 == nums1.__len__():
                    all.append(nums2[n2])
                    n2 = n2 + 1
                elif n2 == nums2.__len__():
                    all.append(nums1[n1])
                    n1 = n1 + 1
                else:
                    if nums1[n1] <= nums2[n2]:
                        all.append(nums1[n1])
                        n1 = n1 + 1
                    else:
                        all.append(nums2[n2])
                        n2 = n2 + 1
            midnum = all[length // 2]
    return midnum

######################################################################
nums1=[1,2,3]
nums2=[2,4,5]
result = findMedianSortedArrays(nums1,nums2)
print(result)