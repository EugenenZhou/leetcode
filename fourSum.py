# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，
# 判断 nums 中是否存在四个元素 a，b，c 和 d ，
# 使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
# 注意：
#
# 答案中不可以包含重复的四元组。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/4sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

######################################################################
def fourSum(nums,target):
    if len(nums) <= 3:
        return []
    nums.sort()
    res = []
    for i in range(len(nums)-3):
        if i != 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,len(nums)-2):
            if j != i+1 and nums[j] == nums[j - 1]:
                continue
            left = j + 1
            right = len(nums)-1
            while left < right:
                s = nums[i] + nums[j] + nums[left] + nums[right]
                if s < target:
                    left = left + 1
                    while left < right and nums[left] == nums[left-1]: left = left + 1
                elif s > target:
                    right = right - 1
                    while left < right and nums[right] == nums[right + 1]: right = right - 1
                elif s == target:
                    res.append([nums[i], nums[j],nums[left],nums[right]])
                    left = left + 1
                    right = right - 1
                    while left < right and nums[left] == nums[left - 1]: left = left + 1
                    while left < right and nums[right] == nums[right + 1]: right = right - 1
    return res

    #两数，三数，四数递归
    # def three_sum(nums, sums, target, low, high, z1):
    #     if low + 1 >= high:
    #         return
    #
    #     if 3 * nums[low] > target or 3 * nums[high] < target:
    #         return
    #
    #     for i in range(low, high + 1):
    #         z = nums[i]
    #         if i > low and nums[i - 1] == nums[i]:
    #             continue
    #         if z + 2 * nums[high] < target:
    #             continue
    #         if 3 * z > target:
    #             break
    #         if 3 * z == target:
    #             if i + 2 <= high and nums[i + 2] == z:
    #                 sums.append([z1, z, z, z])
    #             break
    #
    #         two_sum(nums, sums, target - z, i + 1, high, z1, z)
    #
    # def two_sum(nums, sums, target, low, high, z1, z2):
    #     if low >= high:
    #         return
    #
    #     if 2 * nums[low] > target or 2 * nums[high] < target:
    #         return
    #
    #     left = low
    #     right = high
    #     while left < right:
    #         total = nums[left] + nums[right]
    #         if total == target:
    #             sums.append([z1, z2, nums[left], nums[right]])
    #             while left < right and nums[left] == nums[left + 1]:
    #                 left += 1
    #             while left < right and nums[right] == nums[right - 1]:
    #                 right -= 1
    #             left += 1
    #             right -= 1
    #         elif total < target:
    #             left += 1
    #         else:
    #             right -= 1
    # sums = []
    # if nums is None or len(nums) == 0:
    #     return sums
    #
    # nums.sort()
    # n = len(nums)
    # if 4 * nums[0] > target or 4 * nums[n - 1] < target:
    #     return sums
    #
    # for i in range(n):
    #     z = nums[i]
    #     if i > 0 and nums[i - 1] == nums[i]:
    #         continue
    #     if z + 3 * nums[n - 1] < target:
    #         continue
    #     if 4 * z > target:
    #         break
    #     if 4 * z == target:
    #         if i + 3 < n and nums[i + 3] == z:
    #             sums.append([z, z, z, z])
    #         break
    #
    #     three_sum(nums, sums, target - z, i + 1, n - 1, z)
    #
    # return sums



######################################################################
nums = [1,-2,-5,-4,-3,3,3,5]
target = -11
result = fourSum(nums,target)
print(result)
