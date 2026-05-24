## Find missing value

def find_missing_val(nums):
    n = len(nums)
    for i  in range(n):
        if i not in nums:
            return i

# nums = [1,0,3,4]
# print(find_missing_val(nums))

###################################### Shortcut##################

def finding_missing_value(nums):
    n = len(nums)
    total = (n*(n+1))//2
    rem = total - sum(nums)
    # print(total)
    return rem

nums = [1,0,3,4]
print(finding_missing_value(nums))