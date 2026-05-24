def reverse_array(num, first, last):
    if first >= last:
        return num
    num[first], num[last] =  num[last], num[first]
    # print(num)
    return reverse_array(num, first+1, last-1)



num = [5, 7, 3, 2, 6, 1, 5, 9]  ## Take two pointer and swap first and last element
first = 0
last = len(num)-1
print(reverse_array(num, first, last))