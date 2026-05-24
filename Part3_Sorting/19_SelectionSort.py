def selection_sort(lst):
    min_idx = 0
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if lst[j]<lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

lst = [5,7,8,4,1,6,9,2]
print(selection_sort(lst))
