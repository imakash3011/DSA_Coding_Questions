##  Practice this question

def merge_sorted_array(nums1, nums2):
    res = []
    i, j = 0, 0
    n1, n2 = len(nums1), len(nums2)

    while i < n1 and j < n2:
        # Pick the smaller value
        if nums1[i] < nums2[j]:
            val = nums1[i]
            i += 1
        elif nums2[j] < nums1[i]:
            val = nums2[j]
            j += 1
        else:
            # They are equal, take one and move both pointers
            val = nums1[i]
            i += 1
            j += 1
        
        # Only append if res is empty or val is not a duplicate of the last element
        if not res or val != res[-1]:
            res.append(val)

    # Add remaining elements from nums1
    while i < n1:
        if nums1[i] != res[-1]:
            res.append(nums1[i])
        i += 1

    # Add remaining elements from nums2
    while j < n2:
        if nums2[j] != res[-1]:
            res.append(nums2[j])
        j += 1

    return res

nums1 = [1, 1, 2, 4, 5]
nums2 = [3, 5, 6, 7, 8, 8, 9]
print(merge_sorted_array(nums1, nums2))
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]