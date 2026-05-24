num = 34444443

def check_len(num):
    total_len = 0
    while num>0:
        if num>0:
            total_len+=1
        num = num//10
        
    return total_len

print(check_len(num))

##################################################################################################

## 2 Way (Shortcut)

# import math

# def count_digits(num):
#     if num == 0: 
#         return 1
#     # Handle negative numbers by using absolute value
#     num = abs(num)
#     return math.floor(math.log10(num)) + 1

# print(count_digits(15))   # Output: 2
# print(count_digits(1000)) # Output: 4


