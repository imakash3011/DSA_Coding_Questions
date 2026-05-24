## This is comparing the string at the end of the loop (when string get ends)

# def palindromic_string(str1,first, new_str):
    
#     if first >= len(str1):
#         if new_str == str1:
#             return "Palindromic"
#         else:
#             return "Not Palindromic"
#         # return new_str
#     new_str = str1[first] + new_str 
#     print(new_str)
#     return palindromic_string(str1, first+1, new_str)
    

# str1 = "mom"
# new_str = ""
# print(palindromic_string(str1,0, new_str))

######################################################################

def recursion_palindromic(s1, left, right):
    if left>=right:
        return True
    if s1[left]!=s1[right]:
        return False
    return recursion_palindromic(s1, left+1, right-1)

s1 = "akash"
left = 0
right = len(s1)-1
print(recursion_palindromic(s1, left, right))


#########################################################


# str1 = "akash"
# val = ""
# for i in str1:
#     val = i + val
# print(val)

