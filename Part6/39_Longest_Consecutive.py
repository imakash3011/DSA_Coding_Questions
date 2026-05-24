## Longest Consecutive Sequence (anywhere in array)

def longest_conse_subseq(nums):
    n = len(nums)
    max_cnt = 0
    for i in range(n):
        temp = nums[i]
        cnt = 0
        while temp in nums:
                if temp in nums:
                    temp+=1
                    cnt+=1
        if cnt>max_cnt:
                max_cnt = cnt    
            
    return max_cnt


nums = [1, 99, 101, 102, 103, 2, 5, 3, 100, 1, 1]
print(longest_conse_subseq(nums))



##########################
def longest_conse_subsequence(nums):
    n = len(nums)
    max_cnt = 0
    for i in range(n):
        temp = nums[i]
        cnt = 0
        for j in range(n):
            while temp in nums:
                if temp in nums:
                    temp+=1
                    cnt+=1
            if cnt>max_cnt:
                max_cnt = cnt
    return max_cnt


# nums = [1, 99, 101, 98,102, 103, 2, 5, 3, 100, 1, 1]
# print(longest_conse_subsequence(nums))

