

######################################################################
def two_sum(nums,target):
    hash={}
    for index,num in enumerate(nums):
        if target-num in hash:
            return [hash[target-num],index]
        hash[num]=index
    return None
####################################################################
nums=[2,7,17,15]
target = 5
result=two_sum(nums,target)