class Solution:
    def maxLen(self, arr):
        seen = {}
        prefix_sum = 0
        max_length = 0
        n = len(arr)
        for i in range(n):
            prefix_sum += arr[i]
            if prefix_sum==0:
                max_length+=1
            else:
                if prefix_sum in seen:
                    curr_length = i - seen[prefix_sum]
                    max_length = max(max_length, curr_length)
                else:
                    seen[prefix_sum] = i
        return max_length



arr = [15, -2, 2, -8, 1, 7, 10, 23]
c1 = Solution()
print(c1.maxLen(arr))