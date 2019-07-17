# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
# 找出 nums 中的三个整数，使得它们的和与 target 最接近。
# 返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum-closest
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

######################################################################
def threeSumClosest(nums,target):
    if len(nums) < 3:
        return 0
    nums.sort()
    res = 999999
    for center in range(len(nums)-2):
        left = center + 1
        right = len(nums) - 1
        while left < right:
            s = nums[center] + nums[left] + nums[right]
            if abs(target - s) < abs(target - res):
                res = s
            if s > target:
                right = right - 1
                while left < right and nums[right] == nums[right + 1]: right = right - 1
            elif s < target:
                left = left + 1
                while left < right and nums[left] == nums[left - 1]: left = left + 1
            else:
                return s
    return res

    # res = []
    # nums.sort()
    #
    # for i in range(len(nums) - 2):
    #     if i > 0 and nums[i] == nums[i - 1]: continue
    #     j = i + 1
    #     k = len(nums) - 1
    #     if nums[i] + nums[k] + nums[k - 1] < target:
    #         res.append(nums[i] + nums[k] + nums[k - 1])
    #     elif nums[i] + nums[j] + nums[j + 1] > target:
    #         res.append(nums[i] + nums[j] + nums[j + 1])
    #     else:
    #         while j < k:
    #             s = nums[i] + nums[j] + nums[k]
    #             res.append(s)
    #             if s == target:
    #                 return target
    #             elif s < target:
    #                 j += 1
    #             else:
    #                 k -= 1
    # res.sort(key=lambda x: abs(x - target))
    # return res[0]
######################################################################
numbers = [1,2,5,10,11]
result = threeSumClosest(numbers,12)
print(result)
