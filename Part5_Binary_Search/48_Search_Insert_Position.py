def insert_pos(nums, target):
    left = 0
    right = len(nums)-1


    while left<=right:
        mid = (left+right)//2
        # print(mid)
        if target == nums[mid]:
            return mid
        elif target<nums[mid]:
            right = mid-1
        else:
            left =mid+1
    return left  ## Think of it like.. currently a bigger number it sitting at index one and if we put "target" then it is come towards left and bigger one will move right
   

nums = [1,3,4,5,8,9, 14,15, 19, 20, 21]  ## Unique and sorted elements
target = 2
print(insert_pos(nums, target))