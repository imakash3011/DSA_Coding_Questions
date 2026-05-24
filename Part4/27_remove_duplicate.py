def remove_duplicate(lst):
    # Loop backwards from the second-to-last element to the first
    for i in range(len(lst) - 2, -1, -1):
        if lst[i] == lst[i+1]:
            lst.pop(i + 1) # Remove the item at the next index
    return lst

lst = [1,1,1,2,2,2,3,3,4,5,6,6,7,8,8]   ## Opposite direction looping helps to reduce lst size as well loop range... which helps us to escape out of index error
print(remove_duplicate(lst)) 


############ Here removing duplicate by creating new list ##########
def remove_dup(nums):
    n = len(nums)
    lst =[]
    for i in range(n):
        if nums[i] not in lst:
            lst.append(nums[i])
    return lst

# nums = [1,1,1,2,2,2,3,3,4,5,6,6,7,8,8]
# print(remove_dup(nums))