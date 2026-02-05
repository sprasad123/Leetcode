class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_times = sorted((start, i) for i, (start, end) in enumerate(intervals))
        result = []
        for start, end in intervals:
            i = bisect.bisect_left(start_times, (end,))
            if i < len(start_times):
                result.append(start_times[i][1])
            else:
                result.append(-1)
        return result
        