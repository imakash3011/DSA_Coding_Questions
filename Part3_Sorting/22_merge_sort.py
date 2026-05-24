def merge_sorted_array(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    left, right = 0,0
    result = []
    while left<n and right<m:
        if nums1[left]<nums2[right]:
            result.append(nums1[left])
            left+=1
        else:
            result.append(nums2[right])
            right+=1
    while left<n:
        result.append(nums1[left])
        left+=1
    while right<m:
        result.append(nums2[right])
        right+=1
    return result

def merge_sort_solution(nums):
    if len(nums)<=1:
        return nums
    mid = len(nums)//2
    left_arr = nums[:mid]
    right_arr = nums[mid:]
    left = merge_sort_solution(left_arr)
    right = merge_sort_solution(right_arr)
    return merge_sorted_array(left, right)


# nums1 = [1,2,3,4]
# nums2 = [1,1,3,4,5,6,7]
nums = [3,1,2,4,1,5,2,6,4]
print(merge_sort_solution(nums))