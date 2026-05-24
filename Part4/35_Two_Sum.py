### Single loop solution


def two_sum_index(lst, target):
    n = len(lst)
    for i in range(n):
        rem = target - lst[i]
        if rem in lst[i+1:]:
            second_idx = lst.index(rem, i+1)   ## Remeber this method to get index in a list
            print(lst[i], lst[second_idx])
    

lst = [5,9,1,2,4,15,8,3]
target = 13
print(two_sum_index(lst, target))



#############################################

# def two_sum(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(n):
#             if i!=j and nums[i]+nums[j]==target:
#                 return i, j

# nums = [5,9,1,2,4,15,6,3]
# target = 13
# print(two_sum(nums, target))