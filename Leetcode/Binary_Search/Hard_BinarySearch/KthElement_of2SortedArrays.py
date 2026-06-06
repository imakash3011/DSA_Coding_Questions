'''https://takeuforward.org/plus/dsa/problems/kth-element-of-2-sorted-arrays?source=strivers-a2z-dsa-track'''


################# USING BINARY SEARCH ####################
class Solution:
    def kthElement(self, a, b, k):
        n = len(a)
        m = len(b)
        
        # We always want to perform binary search on the smaller array
        # to ensure the time complexity is O(log(min(n, m)))
        if n > m:
            return self.kthElement(b, a, k)
            
        # Defining boundaries for picking elements from the first array 'a'
        # high: we cannot pick more than 'k' elements or more than the size of 'a'
        # low: if k is larger than the size of 'b', we MUST pick at least k - m elements from 'a'
        low = max(0, k - m)
        high = min(k, n)
        
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = k - mid1
            
            # Left side elements (l1, l2) and right side elements (r1, r2)
            # Use negative and positive infinity to handle edge cases where we pick 0 elements
            l1 = float('-inf') if mid1 == 0 else a[mid1 - 1]
            l2 = float('-inf') if mid2 == 0 else b[mid2 - 1]
            
            r1 = float('inf') if mid1 == n else a[mid1]
            r2 = float('inf') if mid2 == m else b[mid2]
            
            # Valid partition found: the maximum of the left elements is less than 
            # or equal to the minimum of the right elements
            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            
            # If l1 is strictly greater than r2, our partition in 'a' is too far to the right
            elif l1 > r2:
                high = mid1 - 1
                
            # Otherwise, our partition in 'a' is too far to the left
            else:
                low = mid1 + 1
                
        return -1


a = [2, 3, 6, 7, 9] 
b = [1, 4, 8, 10]
k = 2
c1 = Solution()
print(c1.kthElement(a,b,k))


############# BRUTEFORCE APPROACH ########################
class Solution:
    def kthElement(self, a, b, k):
        nums = a+b
        nums.sort()
        return nums[k-1]



# a = [2, 3, 6, 7, 9] 
# b = [1, 4, 8, 10]
# k = 5
# c1 = Solution()
# print(c1.kthElement(a,b,k))