def subset_sum(nums):
    result = []
    def helper_func(idx, subset):
        if idx>=len(nums):
            result.append(subset)
            return
        
        # subset.append(nums[idx])
        helper_func(idx+1, subset + nums[idx])

        helper_func(idx+1, subset)
    
    helper_func(0, 0)
    return result


nums= [5,9,3]
print(subset_sum(nums))



# def subset_sum(nums):
#     result = []
#     def helper_func(idx, subset):
#         if idx>=len(nums):
#             result.append(sum(subset.copy()))
#             return
        
#         subset.append(nums[idx])
#         helper_func(idx+1, subset)

#         subset.pop()
#         helper_func(idx+1, subset)
    
#     helper_func(0, [])
#     return result


# nums= [5,9,3]
# print(subset_sum(nums))
