def palindromic_string(str1, left, right):
    if left>=right:
        return True
    if str1[left]!= str1[right]:
        return False
   
    return palindromic_string(str1, left+1, right-1)

str1 = "mom"
left = 0
right = len(str1)-1
print(palindromic_string(str1, left, right))