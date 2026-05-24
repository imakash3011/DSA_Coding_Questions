def reverse_array(arr, first, last):
    if first>=last:
        return arr
    arr[first], arr[last] =  arr[last], arr[first]
    return reverse_array(arr, first+1, last-1)
    

arr = [1,2,3,4,5]
first = 0
last = len(arr)-1
print(reverse_array(arr, first, last))