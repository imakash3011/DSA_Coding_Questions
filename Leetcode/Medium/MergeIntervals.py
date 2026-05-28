'''
https://leetcode.com/problems/merge-intervals/description/
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()

        result = [intervals[0]]
        for i in range(1, len(intervals)):
            curr_interval = result[-1]
            next_interval = intervals[i]

            if curr_interval[1]>=next_interval[0]:
                curr_interval[1] = max(curr_interval[1], next_interval[1])
            else:
                result.append(next_interval)
        return result


intervals =[[1,3],[2,6],[8,10],[15,18]]
c1 = Solution()
print(c1.merge(intervals))