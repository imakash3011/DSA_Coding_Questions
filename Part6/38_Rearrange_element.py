## Rearrange in positive-Negative Sequence

def rearrange_array(nums):
    n = len(nums)
    even_idx = 0
    odd_idx = 1
    result =[0]*n
    for i in range(n):
        if nums[i]>0 and i<=n:
            result[even_idx] = nums[i]
            even_idx+=2
        else:
            result[odd_idx] = nums[i]
            odd_idx+=2

    return result


nums = [5, 10, -3, -1, -10, 6]
print(rearrange_array(nums))